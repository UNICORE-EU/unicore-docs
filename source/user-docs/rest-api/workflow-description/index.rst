.. _workflow-description:

|workflow-img| Workflow description
-----------------------------------

.. |workflow-img| image:: ../../../_static/workflow.png
	:height: 32px
	:align: middle


Introduction
~~~~~~~~~~~~

This chapter provides an overview of the JSON workflow description that is supported by the 
:ref:`Workflow engine <workflow>`. It will allow you to write workflows *by hand*, i.e. without 
using tools such as the Java or Python APIs.

After presenting all the constructs individually, several complete examples are given in 
:ref:`examples`.


Overview and simple constructs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The overall workflow document has the following form

.. code:: json

  {
	"inputs": {},

	 "activities": {},

	 "subworkflows": {},

	 "transitions": [],

	 "variables": [],

	 "notification": "optional_notification_url",

	 "tags": ["tag1", "tag2", "..." ],
  }

Activities, sub-workflows and transitions make up the workflow logic.

Both activities and sub-workflows are JSON maps (since UNICORE 9.0),
where the key is the unique identifier of the element. The 8.x format
of using JSON arrays with *id* elements is still supported.

Here is a simple example of two tasks that are to be run in a sequence:

.. code:: json

  {
    "activities": {

      "step1": {
        "job": {
          "Executable": "echo step1",
        }
      },

      "step2": {
        "job": {
          "Executable": "echo step2",
        }
      },
    },

    "transitions": [
      {"from": "step1", "to": "step2" }
    ]
  }


The remaining elements in the workflow description are:

- ``inputs`` allows to register external files with the workflow file catalog. See :ref:`datahandling`.
- ``tags`` is an optional list of initial tags, that can later be used to conveniently filter the 
  list of workflows.
- ``notification`` (optional) denotes an URL to where UNICORE Workflow server will send a 
  ``POST`` notification (authenticated via a JWT token signed by the Workflow server) when the 
  workflow has finished processing.

Notification messages sent by the Workflow service have the following content:

.. code:: json
 
  {
    "href" : "workflow_url",

    "group_id": "id of the workflow or sub-workflow",

    "status": "...",

    "statusMessage": "..."
  }

Both of these are analogous to their conterparts for single jobs in UNICORE.

In the next sections the elements of the workflow description will be discussed in detail.

Activities
~~~~~~~~~~

Activity elements have the following form::

	"id": {
	   "type": "...",
         ...
	}

The ``id`` must be UNIQUE within the workflow. There are different types of activity, which
are distinguished by the ``type`` element.

- ``START`` denotes an explicit start activity. If no such activity is present, the processing
  engine detect the proper starting activities.

- ``JOB`` denotes a executable (job) activity. In this case, the job sub element holds the JSON
  job definition (if a ``job`` element is present, you may leave out the ``type``).

- ``MODIFY_VARIABLE`` allows to modify a workflow variable. An option named ``variable_name``
  identifies the variable to be modified, and an option ``expression`` holds the modification
  expression in the Groovy programming language syntax (see also the :ref:`variables section
  <workflow-variables>` later).

- ``SPLIT``: this activity can have multiple outgoing transitions. All transitions with matching
  conditions will be followed. This is comparable to an "*if() … if() … if()*" construct in a
  programming language.

- ``BRANCH``: this activity can have multiple outgoing transitions. The transition with the
  first matching condition will be followed. This is comparable to an "*if() … elseif() … else()*"
  construct in a programming language.

- ``MERGE`` merges multiple flows without synchronising them.

- ``SYNCHRONIZE`` merges multiple flows and synchronises them.

- ``HOLD`` stops further processing of the current flow until the client explicitly sends a
  continue message.


Subworkflows
~~~~~~~~~~~~

The workflow description allows nested sub workflows, which have the same formal structure as
the main workflow (without the ``tags`` and ``inputs``). There is an additional ``type`` element
that is used to distinguish the different control structure types.

.. code:: json

  {

    "id": "unique_id",

    "type": "...",

    "variables": [],

    "activities": {},

    "subworkflows": {},

    "transitions": [],

    "notification" : "optional_notification_url",

  }


Job activities
~~~~~~~~~~~~~~

Job activities are the basic executable pieces of a workflow. The embedded JSON job definition
will be sent to an execution site (UNICORE/X) for processing.

.. code:: json

  {
    "id": "unique_id",

    "type": "job",

    "job": {

      "... standard UNICORE job ...": ""

    },

    "options": {  },
  }

The execution site is specified by the optional ``Site name`` element in the job

.. code:: json

  {
      "id": "unique_id", "type" : "job",

      "job": {

        "Site name": "DEMO-SITE",

      },
  }

.. note::
 There is currently no form of *brokering* in place, it is up to the user to select an execution 
 site.

The job description is covered in detail in :ref:`job-description`.

The processing of the job can be influenced using the (optional) ``options`` sub-element. 
Currently the following options (*key-value*) can be used:

- ``IGNORE_FAILURE`` if set to ``true``, the workflow engine will ignore any failure of the task 
  and continue processing as if the activity had been completed successfully. 
  
  .. note::
    This has nothing to do with the exit code of the actual UNICORE job! Failure means for example 
    data staging failed, or no matching target system for the job could be found.

- ``MAX_RESUBMITS`` set to an integer value to control the number of times the activity will be 
  retried. By default, the workflow engine will re-try three times (except in those cases where 
  it makes no sense to retry).

For example,
::

	{
	 "id": "unique_id",

	 "job" : {

	  ... standard UNICORE job ...

	 },

	 "options": { "IGNORE_FAILURE": "true",  },
	}

If you need to pass on user preferences to the site, e.g. for selecting your primary group, or 
choosing between multiple user IDs, you can specify this in the ``job`` element like this::

 ...

 "job": {

    "User prefences": {
      "uid":   "hpcuser21",
      "group": "hpc",
    }

 }
 ...


where the allowed field names are ``role``, ``uid``, ``group`` and ``supplementaryGroups``.

.. _datahandling:

Data handling
~~~~~~~~~~~~~

One of the most common tasks is linking the output of one activity to another activity for
further processing. The UNICORE workflow system supports this by providing a per-workflow
file catalog, where jobs can reference files with special URIs starting with ``wf:``.

Jobs can register outputs with the file catalog using stage-out directives, for example,
::

   Exports: [
     { "From": "stdout", "To": "wf:step1_stdout" }
   ]

will register the ``stdout`` file under the name *wf:step1_stdout* (note that the file will not be
copied anywhere).

Later jobs can reference files from the catalog using stage-in directives, for example,
::

   Imports: [
     { "From": "wf:step1_stdout", "To": "input_file" }
   ]

The workflow engine will take care of resolving the ``wf:...`` reference to the actual physical location.

Apart from registration of files in jobs, the user can also *manually* register files using the 
``inputs`` section of the main workflow:
::

  "inputs": {
    "wf:input_data_1": "https://some_storage/somefile.pdf",
    "wf:input_params": "https://some_storage/parameters.txt"
  }


For an example of a workflow, have a look at :ref:`examples_two_step_with_data`.

The Workflow REST API allows you to list (and modify) the file catalog via 
the ``BASE/{id}/files`` endpoint.


Transitions and conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The basic flow of control in a workflow is handled using transition elements. These reference 
from and to activities or subflows, and may have conditions attached. If no condition is present, 
the transition is followed unconditionally, otherwise the condition is evaluated and the 
transition is followed only if the condition matches (i.e. evaluates to true).

The syntax for a Transition is as follows:
::

	{

	  "from" : "from_id",

	  "to" : "to_id",

	  "condition": "expression"

	}

The ``from`` and ``to`` elements denote activity or subworkflow id’s.

An activity can have outgoing (and incoming) transitions. In general, all outgoing transitions 
(where the condition is fulfilled) will be followed. The exception is the ``Branch`` activity, 
where only the first matching transition will be followed.

The optional condition element is a string-valued expression. The workflow engine offers some 
pre-defined functions that can be used in these expressions. For example, you can use the exit 
code of a job, or check for the existence of a file within these expressions.

- ``eval(expr)`` Evaluates the expression *expr* in Groovy syntax, which must evaluate to a 
  boolean. The expression may contain workflow variables.

- ``exitCodeEquals(activityID, value)`` Allows to compare the exit code of the UNICORE job 
  associated with the Activity identified by *activityID* to *value*.

- ``exitCodeNotEquals(activityID, value)`` Allows to check the exit code of the UNICORE job 
  associated with the Activity identified by *activityID*, and check that it is different from 
  *value*.

- ``fileExists(activityID, fileName)`` Checks that the working directory of the UNICORE job 
  associated with the given Activity contains a file *fileName*.

- ``fileLengthGreaterThanZero(activityID, fileName)`` Checks that the working directory of the 
  UNICORE job associated with the given Activity contains the named file, which has a non-zero 
  length.

- ``before(time)`` and ``after(time)`` check whether the current time is before or after the 
  given time (in *yyyy-MM-dd HH:mm* format).

- ``fileContent(activityID, fileName)`` Reads the content of the named file in the working 
  directory of the job associated with the given Activity and returns it as a string.


.. _workflow-variables:

Using workflow variables
~~~~~~~~~~~~~~~~~~~~~~~~

Workflow variables need to be declared using an entry in the ``variables`` array before they can be 
used.
::

	{

	  "name": "...",

	  "type": "...",

	  "initial_value": "..."

	}

Currently variables of type ``STRING``, ``INTEGER`` , ``FLOAT`` and ``BOOLEAN`` are supported.

Variables can be modified using an activity of type ``MODIFY_VARIABLE``.

For example, to increment the value of the *COUNTER* variable, the following Activity is used
::

	{

	 "type": "MODIFY_VARIABLE",

	 "id": "incrementCounter",

	 "variable_name": "COUNTER",

	 "expression": "COUNTER += 1;"

	}

The ``expression`` contains an expression in Groovy syntax (which is very close to Java).

The workflow engine will replace variables in job data staging sections and environment 
definitions, allowing to inject variables into jobs. Examples for this mechanism will be given 
in the :ref:`examples` section.

Loop constructs
~~~~~~~~~~~~~~~

Apart from graphs constructed using ``activity`` and ``transition`` elements, the workflow system 
supports special looping constructs, *for-each*, *while* and *repeat-until*, which allow to build 
complex workflows.

*While* and *repeat-until* loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These allow to loop a certain part of the workflow while (or until) a condition is met. 
A *while* loop looks like this
::

	{
	 "id": "while_example",

	 "type" : "WHILE",

	 "variables" : [
	  {
		"name": "C",
		"type": "INTEGER",
		"initial_value": "1",
	  }
	 ],

	 "body":
	  {
	   "activities": {
	     "task" : {
		    "job": { ... }
	    },
	    "mod": {
		  # this modifies the variable used in the 'while'
		  # loop's exit condition
		  "type": "MODIFY_VARIABLE",
		  "variable_name": "C",
		  "expression": "C++;",
	    }
	   },

	   "transitions: [
		 {"from": "task", "to": "mod"}
	   ]
	  },
	  
	 "condition": "eval(C<5)",
	  
	}

The necessary ingredients are that the loop’s ``body`` modifies the loop variable ("C" in the 
example), and the exit condition eventually terminates the loop.

For a full workflow example, see :ref:`examples_while_loop`.


Completely analogously to the *while* loop, a *repeat-until* loop is constructed, the only
syntactic difference is that the subworkflow now has a different type element::

	{
	  "id": "repeat_example",

	  "type": "REPEAT_UNTIL",

	  ...
	}

Semantically, the *repeat*-loop will always execute the body at least once, since the condition is 
checked after executing the body, while in the *while* case, the condition will be checked before 
executing the body.

*For-each* loop
^^^^^^^^^^^^^^^

The *for-each* loop is a complex and powerful feature of the workflow system, since it allows 
parallel execution of the loop body, and different ways of building the different iterations. 
Put briefly, one can loop over variables (as in the *while* and *repeat-until* case), but one 
can also loop over enumerated values and (most importantly) over file sets.

The basic syntax is:
::

	{
	 "id": "for_each_example",

	 "type": "FOR_EACH",

	 "iterator_name": "IT",

	 "body": {

	 },

	# define range to loop over

	 "values": [...],

	# OR variables

	 "variables": [...],

	# OR files

	 "filesets": [...],

	  # with optional chunking
	 "chunking":

	}

The ``iterator_name`` element allows to control how the *loop iterator variable* is to be called, 
by default it is named *IT*.

The ``values`` element
^^^^^^^^^^^^^^^^^^^^^^

Using value, iteration over a fixed set of strings can be defined. The main use for this is 
parameter sweeps, i.e. executing the same job multiple times with different arguments or 
environment variables.
::

 "values": ["1", "2", "3", ],


The following variables are set where ``IT`` is the loop ``iterator_name`` defined
in the for group as shown above:

- ``IT`` is set to the current iteration index (1, 2, 3, …)

- ``IT_VALUE`` is set to the current value


The ``variables`` element
^^^^^^^^^^^^^^^^^^^^^^^^^

The ``variables`` element allows to define the iteration range using one or more variables, 
similar to a for-loop in a programming language.
::

	"variables: [
	 {
	   "variable_name": "X",
	   "type": "INTEGER",
	   "start_value": "0",
	   "expression": "Y++",
	   "end_condition": "Y<2"
	 },
	 {
	   "variable_name": "Y",
	   "type": "INTEGER",
	   "start_value": "0",
	   "expression": "Y++",
	   "end_condition": "Y<2"
	 }
	],

The sub-elements should be self-explanatory.

Note that you can use more than one variable range, allowing you to quickly create things like 
parameter studies.

The following variables are set where ``IT`` is the loop ``iterator_name`` defined
in the for group as shown above:

- ``IT`` is set to the current iteration index (1, 2, 3, …)

- ``IT_VALUE`` is set to the current value



The ``file_sets`` element
^^^^^^^^^^^^^^^^^^^^^^^^^

This variation of the *for-each* loop, allows to loop over a set of files, optionally chunking 
together several files in a single iteration.

The basic structure of a file set definition is this:
::

	"file_sets": [

	 {
	  "base": "...",
	  "include": [ "..." ],
	  "exclude": [ "..." ],
	  "recurse": "true|false",
	  "indirection": "true|false",
	},

	]

The base element defines a base of the filenames, which will be resolved at runtime, and 
complemented according to the include and/or exclude elements. The ``recurse`` attribute allows 
to control whether the resolution should be done recursively into any subdirectories. The 
indirection attribute is explained below.

For example, to recursively collect all PDF files (except two files named *unused\*.pdf*) in a 
certain directory on a storage::

	"file_sets": [

	 {
		"base": "https://mysite/rest/core/storages/my_storage/files/pdf/</s:Base>
		"include": [ "*.pdf" ],
		"exclude": [ "unused1.pdf", "unused2.pdf", ],
		"recurse": "true"
	  }

	]

The following variables are set where ``IT`` is the loop ``iterator_name`` defined
in the for group as shown above:

- ``IT`` is set to the current iteration index (1, 2, 3, …)

- ``IT_VALUE`` is set to the current full file path

- ``IT_FILENAME`` is set to the current file name (last element of the path)


Indirection
^^^^^^^^^^^

Sometimes the list of files that should be looped over is not known at workflow design time, but 
will be computed at runtime. Or, you wish simply to list the files in a file, and not put them 
all in your workflow description. The ``indirection`` attribute on a FileSet allows to do just that. 
If ``indirection`` is set to ``true``, the workflow engine will load the given file(s) in the 
fileset at runtime, and read the actual list of files to iterate over from them. As an example, 
you might have a file filelist.txt containing a list of UNICORE file URLs::

	https://someserver/file1
	https://someserver/fileN
	...

and the fileset
::

	{
	   "indirection": "true",
	   "base": "https://someserver/rest/core/storages/mystorage/files/</s:Base>
	   "include": [ "filelist.txt" ],
	}

You can have more than one file list.

Chunking
^^^^^^^^

Chunking allows to group sets of files into a single iteration, for example for efficiency 
reasons.

A chunk is either a certain number of files, or a set of files with a certain total size.
::

 "chunking": {
  "chunksize": ... ,
  "type": "NORMAL|SIZE",
  "filename_format": "...,
  "expression": "... formula to compute chunksize ...",
 }

The ``chunksize`` element is either the number of files in a chunk, or (if type is set to ``SIZE``) 
the total size of a chunk in kbytes.

For example,

 - To process 10 files per iteration::

	"chunking":
	{
	  "chunksize": "10",
	}

 - To process 2000 kBytes of data per iteration::

	"chunking":
	{
	  "chunksize": "2000",
	  "type": "SIZE"
	}

The ``chunksize`` can also be computed at runtime using the expression given in the optional 
expression element. In the expression, two special variables may be used. The ``TOTAL_NUMBER`` 
variable holds the total number of files iterated over, while the ``TOTAL_SIZE`` variable holds 
the aggregated size of all files in kbytes. The script must return an integer-valued result. 
The ``type`` element is used to choose whether the chunk size is interpreted as number of files or 
data size.

For example, to choose a larger chunksize if a certain total file size is exceeded::

	"chunking": {
	  "expression": "if(TOTAL_SIZE>50*1024)return 5*1024 else return 2048;"
	  "type": "SIZE"
	}

The optional ``filename_format`` allows to control how the individual files (which are staged into 
the job directory) should be named. By default, the index is prepended, i.e. an import statement
like
::

  "Imports": [{ "From": "${IT_VALUE}", "To" : "infile.txt" }]

would result in *1_infile.txt* to *N_infile.txt* in each chunk. 
In the ``filename_format`` pattern you can use the variables ``{0}``, ``{1}`` and ``{2}``, 
which denote the index, filename without extension and extension respectively. 
::

  {0} = 1, 2, 3, ...
  {1} = "infile"
  {2] = "txt"

For example, if you have a set of PDF files, and you want them to be 
named *file_1.pdf* to *file_N.pdf*, you could use the pattern:
::

  "filename_format": "file_{0}.pdf"

which would ignore the original filename in the ``To`` field completely.
Or, if you prefer to keep the existing extensions, but append an index to the name, use
::

  "filename_format": "{1}{0}.{2}"

which would result in filenames like below:
::

  inputfile1.txt
  inputfile2.txt
  ...

You can also keep the original filenames by setting:
::
  
   "Imports": [{ "From": "${IT_VALUE}", "To" : "${IT_ORIGINAL_FILENAME}"}]


The following variables are set where ``IT`` is the loop ``iterator_name`` defined
in the for group as shown above:

- ``IT`` is set to the current iteration index (1, 2, 3, …)

- ``IT_VALUE`` is set to the current full file path

- ``IT_ORIGINAL_FILENAME_x`` is set to the current file name (last element of the path)

- ``IT_ORIGINAL_FILENAMES`` is set to a ";"-separated list of all the
  file names (last elements of the paths) in the current chunk


.. _examples:

Examples
~~~~~~~~

This section collects a few simple example workflows. They are intended to be submitted using 
:ref:`ucc`.

.. _examples_two_step_with_data:

Simple *two-step* workflow with data dependency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This example shows how to link output from one task to the input of another task using
the internal file catalog.

The first task, *step1*, registers its ``stdout`` with the file catalog under the name
``wf:step1_out``, and the second task, *step2*, pulls that file in for further processing.
::

	{
	  "activities": {

	    "step1": {
	      "job": {
	        "ApplicationName": "Date",
	        "Exports": [
	          {"From": "stdout", "To": "wf:step1_out"}
	        ]
	      }
	    },

	    "step2": {
	      "job": { 
	        "Executable": "md5sum", 
	        "Arguments": ["infile" ],
	        "Imports": [
	          { "From": "wf:step1_out", "To": "infile"}
	        ]  
	      }
	    }
	  
	  },
	  
	  "transitions": [
	    {"from": "step1", "to": "step2" }
	  ]
	}


Simple *diamond* graph
^^^^^^^^^^^^^^^^^^^^^^

This example shows how to use transitions for building simple workflow graphs. It consists of 
four *Date* jobs arranged in a diamond shape, i.e. *date2a* and *date2b* are executed (more 
or less) simultaneously.
::

	{
	 "activities": {

	   "date1": {
	      "job": { "ApplicationName": "Date" }
	   },

	   "date2a": {
	      "job": { "ApplicationName": "Date" }
	   },

	   "date2b": {
	      "job": { "ApplicationName": "Date" }
	   },

	   "date3": {
	      "job": { "ApplicationName": "Date" }
	   }

	 },

	 "transitions": [
	   {"from": "date1", "to": "date2a" },
	   {"from": "date1", "to": "date2b" },
	   {"from": "date2a", "to": "date3" },
	   {"from": "date2b", "to": "date3" }
	 ]
	}

Conditional execution in an *if-else* construct
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transitions from one activity to another may be conditional, which allows all sorts of *if-else* 
constructs. Here is a simple example::

	{

	  "activities": {

	    "branch": { "type": "BRANCH" },

	    "if-job": {
	       "job": { "ApplicationName": "Date" }
	    },

	    "else-job": {
	       "job": { "ApplicationName": "Date" }
	    }

	  },

	  "transitions": [
	    {"from": "branch", "to": "if-job", "condition": "2+2==4"},
	    {"from": "branch", "to": "else-job" }
	  ]

	}

Here we use the ``BRANCH`` activity which will only follow the first matching transition.


.. _examples_while_loop:

*While* loop example using workflow variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The next example shows some uses of workflow variables in a *while* loop. The loop variable *C* is 
copied into the job’s environment. Another possible use is to use workflow variables in data 
staging sections, for example to name files.
::

	{

	  "activities":{},

	  "subworkflows": {

	   "while-example": {

		"type": "WHILE",

		"variables": [
		 {
		   "name": "C",
		   "type": "INTEGER",
		   "initial_value": "0"
		 }
		],

		"condition": "C<5",

		"body": {

		   "activities": {

		   "job": {
			 "job": {
				"Executable": "echo",
				"Arguments": ["$TEST"],
				"Environment": ["TEST=${C}"],
				"Exports": [
				  { "From": "stdout", "To": "wf:/out_${C}" }
				]
			  }
		    },

		    "mod": {
			   "type": "MODIFY_VARIABLE",
			   "variable_name": "C",
			   "expression": "C++"
		    }

		   },

		   "transitions": [
			  {"from": "job", "to": "mod" }
		   ]
		}

	   }
	  
	  }
	
	}


*For-each* loop example
^^^^^^^^^^^^^^^^^^^^^^^

The next example shows how to use the *for-each* loop to loop over a set of files. The jobs will 
stage-in the current file. Also, the name of the current file is placed into the job environment.
::

	{
	
	  "subworkflows": {
	  
	   "for-example": {
		  "type": "FOR_EACH",
		  "iterator_name": "IT",
		
		"body":
		  {
			"activities": {
			
			  "job": {
				"id": "job",
				"job": {
				 "Executable": "echo",
				 "Arguments": ["processing: ", "$NAME"],
				 "Environment": ["NAME=${IT_FILENAME}"],
				 "Imports": [
				   {"From": "${IT_VALUE}", "To": "infile"}
				 ],
				 "Exports": [
				   {"From": "stdout", "To": "wf:/out_${IT}"}
				 ]
				}
			  }
			  
			},
			
		  },
		  
		"filesets": [
		  {
			"base": "https://mygateway.de:7700/MYSITE/rest/core/storages/my_storage/",
			"include": ["*"],
		  }
		]
		
	   }
	   
	  }
	
	}
