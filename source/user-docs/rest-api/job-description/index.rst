.. _job-description:

Job description format
----------------------

A UNICORE job describes a *single job* on the target system.

By default, the job will be submitted to the batch system and run on a compute node.
However, UNICORE supports :ref:`other job types<jd_job_types>` as well.

UNICORE uses a JSON format that allows you to specify the application or executable you want to 
run, arguments and environment settings, any files to stage in from remote servers and any result 
files to stage out. Depending on the client, the JSON may also contain additional instructions 
that are relevant to that client, so make sure to check the client manuals as well.


Overview
~~~~~~~~

UNICORE's job description consists of several parts (their order does not matter):

- an ``Imports`` section listing data to be staged in to the job's working directory from remote 
  storage locations (and/or the client's file system, if you use :ref:`UCC<ucc>`)
- pre-processing
- a section describing the main executable
- post-processing
- an ``Exports`` section listing result files to be staged out to remote storage locations
- a ``Resources`` section stating any resource requirements like batch queue, job runtime or number 
  of nodes
- a number of additional elements for setting the job name, or defining tags for the job

Here is a table listing the supported elements, these will be described in more detail below.

.. include:: tables/job-desc.rest


Job elements
~~~~~~~~~~~~

.. _jd_job_types:

Job types
^^^^^^^^^

UNICORE supports four types if jobs. They are selected by the ``Job type``
element. If not given, ``batch`` is the default.


 * ``batch`` (or ``normal``) - this is the default. UNICORE submits the job to the batch system.
   After being scheduled, the launched on the requested number of compute nodes.
   The job's resource requests (like number of nodes or requested run time) are taken
   from the job's ``Resources`` section.

 * ``on_login_node`` (or ``interactive``) - the user job will be launched on a login node.
   If applicable, you can select the login node with the ``Login node`` element.
   
 * ``raw`` - the job goes to the batch system, but the resources are taken from an additional file,
   which contains BSS directives (e.g."#SBATCH ..." in the case of Slurm.
   
 * ``allocate`` - this is basically the same as "batch", but it only creates an allocation on
   the batch system, without launching any user tasks. You can submit tasks "into" the allocation
   later.


Specifying the executable or application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To directly call an executable on the remote system:

.. code:: json

	{
	   "Executable": "/bin/date",  
	}

You can specify a UNICORE application (defined in the server's IDB) by name and (optional) 
version:

.. code:: json

	{
	   "ApplicationName": "Date",
	   "ApplicationVersion": "1.0",  
	}

Note the comma-separation and the curly braces.


Arguments and Environment settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arguments and environment settings are specified using a list of String values. Here is an 
example.

.. code:: json

	{

	   "Executable": "/bin/ls",

	   "Arguments": ["-l", "-t"],

	   "Environment": [ "PATH=/bin:$PATH", "FOO=bar" ],

	}


Argument sweeps
^^^^^^^^^^^^^^^

To create a sweep over an Argument setting by replacing the value by a sweep specification. This 
can be either a simple list:

::

  "Arguments": [
   { "Values": ["-o 1", "-o 2", "-o 3"] },
  ],  

or a range:

::

  "Arguments": {
   "-o", { "From": "1", "To": "3", "Step" : "1" },
  },  

where the ``From``, ``To`` and ``Step`` parameters are floating point or integer numbers.


Application parameters
^^^^^^^^^^^^^^^^^^^^^^

In UNICORE, parameters for applications are often transferred in the form of environment variables. 
For example, the POVRay application has a large set of parameters to specify image width, height and 
many more. You can specify these parameters in a very simple way using the ``Parameters`` keyword:

.. code:: json

	{
	  "ApplicationName": "POVRay",

	  "Parameters": {
	   "WIDTH": "640",
	   "HEIGHT": "480",
	   "DEBUG": "",
	  },  

	}

Note that an *empty* parameter (which does not have a value) needs to be written with an explicit
empty string due to the limitations of the JSON syntax.


Parameter sweeps
^^^^^^^^^^^^^^^^

You can sweep over application parameters by replacing the parameter value
by a sweep specification. The replacement can be either a simple list:
::

  "Parameters": {
   "WIDTH": { "Values": ["240", "480", "960"] },
  },  

or a range:
::

  "Parameters": {
   "WIDTH": { "From": "240", "To": "960", "Step": "240" },
  },  

where the ``From``, ``To`` and ``Step`` parameters are floating point or integer numbers.


Job data management
~~~~~~~~~~~~~~~~~~~

In general, your job will require data files either from your client machine or from some 
remote location. An important concept in UNICORE is the job's workspace, which is the default 
location into which files are placed. The same applies to result files: by default, files will be 
downloaded from the job's workspace. However, other remote storage locations are supported, too.


Jobs without client-controlled stage in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To tell UNICORE/X that the client does not wish to send any local files, use the flag
::

 "haveClientStageIn": "false",

Otherwise, the server will wait for an explicit *start* command (see the :ref:`rest-api` spec for 
details) before submitting / executing the user job.


Importing files into the job workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To import files from remote sites to the job's working directory on the remote UNICORE server, 
there's the ``Imports`` keyword. Here is an example of ``Imports`` section which demonstrates 
some of the possibilities.

Note that uploading LOCAL files is the responsibility of the client! Make sure to read the 
:ref:`client documentation <ucc-manual>` for more information on this topic.

.. code:: json

	{
	"Imports": [ 

	 { 
	  "From": "UFTP:https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/testfile",
	  "To":   "testfile" },

	{ 
	  "From": "link:/work/data/testfile", 
	  "To": "linked-file" },

	 {
	 "From": "link:/work/data/testfile", 
	 "To": "copied-file" },

	],
	}

If you want the job to run even if an import operation fails, there is a flag ``FailOnError`` 
that can be set to ``false``:

.. code:: json

 { 
    "From":        "/work/data/fileName",
    "To":          "fileName",
    "FailOnError": "false",
 }

Special protocols for imports:

- ``file://`` : copy file(s) residing on the remote machine into the job dir
- ``link://`` : symlink a file/dir residing on the remote machine into the job dir
- ``ftp://`` : download a file from an FTP server
- ``https://`` : download a file from an HTTP(s) server (UNICORE will try to *guess* whether the 
  HTTP URL refers to a UNICORE file or not)


Using *inline* data to import a file into the job workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For short import files, it can be convenient to place the data directly into the job description,
which can speed up and simplify the job submission process.

Here is an example:

.. code:: json

	{
	  "To":   "uspaceFileName",
	  "Data": "this is some test data"
	}

In this case, the ``From`` URL is not needed. If you give one, it HAS to start with ``inline://``,
the rest is not important. Make sure to properly escape any special characters.

Sweeping over a stage-in file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also sweep over files, i.e. create multiple batch jobs that differ by one imported file. 
To achieve this, replace the ``From`` parameter by list of values, for example:

.. code:: json

    { 
      "From": [ 
               "https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/file1", 
               "https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/file2", 
               "https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/file3", 
               ],
      "To": "fileName"
    }

Note that only a single stage-in can be sweeped over in this way, and that this will not work 
with files imported from your local client machine.


Exporting result files from the job workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To export files from the job's working directory to remote storages, use the ``Exports`` keyword.

.. note::
 Depending on the client, additional options exist, such as downloading files to your local 
 machine.

Here is an example:

.. code:: json

	{
	  "Exports": [ 

		{ 
		  "From": "stdout", 
		  "To":   "https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/results/myjob/stdout" 
		},

		{ 
		  "From": "results.dat", 
		  "To":   "https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/results/myjob/results.dat" 
		},

	  ],
	}

Specifying credentials for data staging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some data staging protocols supported by UNICORE require credentials such as username and password.

To pass username and password to the server, the syntax is as follows:

.. code:: json

     { 
       "From": "ftp://someserver:25/some/file", 
       "To": "input_data",
       "Credentials": { "Username": "myname", "Password": "mypassword" },
     }

and similarly for exports.

You may also directly specify an OAuth Bearer token for HTTPS data transfers.

.. code:: json

     { 
       "From": "https://someserver/some/file", 
       "To": "input_data",
       "Credentials": { "BearerToken": "some_token" },
     }

You can leave the token value empty, set to "", if the server already has your token by some 
other means.

Redirecting standard input
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to have your application or executable read its standard input from a file, you
can use the following
::

  "Stdin": "filename",

then the standard input will come from the file named *filename* in the job working directory.

Resources
~~~~~~~~~

A job definition can have a ``Resources`` section specifying the resources to request
on the remote system. For example,

.. code:: json

  {
    "Resources": {

      "Queue" : "fast",  
      "Runtime": "12h",  
      "Nodes": "8",

    }
  }

UNICORE has the following built-in resource names:

.. include:: tables/resources.rst

..
 .. csv-table::
  :file: tables/resources.csv
  :widths: 30, 70
  :header-rows: 1
  :class: tight-table

Sites may define additional, *custom* resources, which you can use, too.


Miscellaneous options
~~~~~~~~~~~~~~~~~~~~~

Specifying a project
^^^^^^^^^^^^^^^^^^^^

If the system you're submitting to requires a project name for accounting purposes, you 
can specify the account (or project) you want to charge the job to using the ``Project`` tag:
::

  "Project" : "my_project",

Job tags
^^^^^^^^

To set job tags that help you find / filter jobs later, use the ``Tags`` keyword
::

  "Tags": [ "production", "train1", "my_tag" ],


Specifying a URL for receiving notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The UNICORE/X server can send out notifications when the job enters the ``RUNNING`` and/or 
``DONE`` state.
::

  "Notification" : "https://your-service-url",

UNICORE/X will send an authenticated ``HTTPS POST`` message to this URL, with JSON content.

.. code:: json

   {
	"href" : "https://unicore-url/rest/core/jobs/job-uuid",
	"status" : "RUNNING",
	"statusMessage" : ""
   }

The ``status`` field will be ``RUNNING`` when the user application starts executing, and 
``SUCCESSFUL`` / ``FAILED`` when the job has finished.

.. code:: json

   {
	"href" : "https://unicore-url/rest/core/jobs/job-uuid",
	"status" : "SUCCESSFUL",
	"statusMessage" : "",
	"exitCode" : 0
   }

Do not expect *realtime* behaviour here, as UNICORE has a certain delay (typically 30 to 60 
seconds, depending on the server configuration) until *noticing* job status changes on the batch 
system.

If you want to verify that the sender of the notification is really UNICORE/X, you will need to 
check and validate the JWT Bearer token UNICORE/X sends in the Authorization header.

Specifying the job name
^^^^^^^^^^^^^^^^^^^^^^^

The job name can be set simply by
::

  "Name": "Test job",

Specifying the user email for batch system notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some batch systems support sending email upon completion of jobs. To specify
your email, use
::

  "User email": "foo@bar.org",

