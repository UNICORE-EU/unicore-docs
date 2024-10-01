.. _job-description:

|job-desc-img| Job description format
-------------------------------------

.. |job-desc-img| image:: ../../../_static/job-desc.png
	:height: 32px
	:align: middle
	
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

UNICORE supports four types of jobs. They are selected by the ``Job type``
element. If not given, ``batch`` is the default.


 * ``batch`` (or ``normal``) - this is the default. UNICORE submits the job to the batch system.
   After being scheduled, the specified executable is launched on the requested number of compute nodes.
   The job's resource requests (like number of nodes or requested run time) are taken
   from the job's ``Resources`` section.

 * ``on_login_node`` (or ``interactive``) - the specified executable will be launched on a login node.
   If you want, you can select the login node with the ``Login node`` element.
   
 * ``raw`` - the job goes to the batch system, but the resources are taken from an additional file,
   which contains BSS directives (e.g.``#SBATCH ...`` in the case of Slurm).
   The name of the file containing BSS directives is given via the ``BSS file`` element.
   
 * ``allocate`` - this is basically the same as *batch*, but it only creates an allocation on
   the batch system, without launching any user tasks. You can submit tasks *into* the allocation
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


Pre- and postprocessing
^^^^^^^^^^^^^^^^^^^^^^^

In addition to the main executable (or application), a UNICORE job can contain
pre- and/or postprocessing tasks that are run before / after the main executable.

The main elements for this are

 * ``User precommand`` - this will be run after the data stage-in and before the main
   executable

 * ``User postcommand`` - this will be run after the main executable and before starting to
   stage-out data
    
For example

.. code:: json

	{
	  "User precommand": "./preprocessing.sh",
	  
	  "Executable": "./main.sh",
	  
	  "User postcommand": "./post-processing.sh"

	}

The pre/post commands will be run on a login node by default. Failure of the pre/post
commands will cause the job to fail.

The default behaviour can be modified via the following options:

 * ``RunUserPrecommandOnLoginNode: 'false'`` - add pre processing as a prolog to the main
   job script

 * ``UserPrecommandIgnoreNonZeroExitCode`` - don't fail the job if the pre command exits with a
   non-zero exit code

 * ``Login node`` - select a preferred login node

and the same for the post command.

Job data management
~~~~~~~~~~~~~~~~~~~

In general, your job will require data files either from your client machine or from some 
remote location. Also, result files and other output files need to be accessible, or need
to be exported (staged out) when the user task has finished executing.

Most of the job data management will be handled via the job's workspace, which is a unique,
per-job directory that UNICORE creates when the job is submitted, and that is linked to the
job. The job directory can be accessed at any time during the job's life time.


Jobs without client-controlled stage in
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some jobs require additional files from the client machine to be uploaded before the
user task can be started.

Uploading LOCAL files is the responsibility of the client! Make sure to read the 
:ref:`client documentation <ucc-manual>` for more information on this topic.

To tell UNICORE/X that the client does not wish to send any local files, use the flag
::

 "haveClientStageIn": "false",

Otherwise, the server will wait for an explicit *start* command (see the :ref:`rest-api` spec for 
details) before submitting / executing the user task.


Importing files into the job workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To import (i.e. stage in) files from remote sites to the job's working directory on the remote UNICORE server, 
there's the ``Imports`` keyword. Here is an example of ``Imports`` section which demonstrates 
some of the possibilities.

.. code:: json

  {
    "Imports": [
      {
        "From": "UFTP:https://gw:8080/DEMO-SITE/rest/core/storages/HOME/files/testfile",
        "To":   "testfile"
      },
      {
        "From": "link:/work/data/testfile",
        "To":   "linked-file"
      },
      {
        "From": "link:/work/data/testfile",
        "To":   "copied-file"
      }
    ]
  }

An Import can have the following elements.

.. code:: json

  {
    "From": "source-url",
    "To":   "target-path",
    "FailOnError": "true | false",
    "Permissions": "unix-style-rwx-permissions",
    "Credentials": { },
    "ExtraParameters": { },
    "Mode": "overwrite | append | nooverwrite",
  }

The mandatory ``From`` element is a URL denoting the source of the file(s).
UNICORE knows the following stage-in protocols:

- ``https://``  : download a file from an HTTP(s) server (UNICORE will try to *guess* whether the
  HTTP URL refers to a UNICORE file or not)
- ``file://``   : copy file(s) residing on the remote machine into the job dir
- ``link://``   : symlink a file/dir residing on the remote machine into the job dir
- ``ftp://``    : download a file from an FTP server
- ``git:``      : download the files from the given git repository
- ``inline://`` : ascii data is given directly, see below

The mandatory ``To`` element is the target path.  As usual in UNICORE, this is relative
to the base directory of the storage endpoint, in this case the job working
directory. You can import into sub-directories, if these do not exist,
they will be created as needed.

The optional flag ``FailOnError`` lets you you control if the job
should continue even if an import operation fails. To do that, set this
flag to ``false``:

.. code:: json

 { 
    "From":        "/work/data/fileName",
    "To":          "fileName",
    "FailOnError": "false",
 }

The optional ``Permissions`` element allows you to explicitely set file permissions.


.. code:: json

 {
    "From":        "/work/data/fileName",
    "To":          "myscript.sh",
    "Permissions": "r-xr--r--"
 }

(An abbreviated version like "r-x" also works).

The optional ``Mode`` element has three valid options: "overwrite" (default) will simply
write the file. "append" will append if existing, and "nooverwrite" will fail if the
file already exists.

The optional ``Credentials`` element can hold e.g. a required username/password
and is discussed below.

The optional ``ExtraParameters`` element is used for protocol-specific extra settings.


Using *inline* data to import a file into the job workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For short import files, it can be convenient to place the data directly into the job description,
which can speed up and simplify the job submission process.

Here is an example:

.. code:: json

  {
    "To":   "myscript.sh",
    "Data": [
      "this is some test data",
      "multi line data",
      "another line"
    ]
  }

In this case, the ``From`` URL is not needed. If you give one, it has to start with ``inline://``,
the rest is not important. 

Make sure to properly escape any special characters.

Staging in from *git*
^^^^^^^^^^^^^^^^^^^^^

You can stage-in a git repository, optionally allowing you to choose a
particular commit, and to pass any required credentials.

For example

.. code:: json

  {
    "From": "git:https://github.com/github/testrepo.git",
    "To":   "testrepo",
    "ExtraParameters": {
      "commit" : "26fc7091"
    },
    "Credentials": { 
      "Password" : "some_api_token",
      "Username" : "test"
    }
  }

If the git repo contains any submodules, these will be downloaded as well.

Please note that this operation will not result in a functional git repo,
only the files will be downloaded.

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
    ]
  }

An Export can have the following elements.

.. code:: json

  {
    "From": "file-path",
    "To":   "target-URL",
    "FailOnError": "true | false",
    "Credentials": { },
    "ExtraParameters": { },
  }

The mandatory ``To`` element is a URL denoting the target of the export.
UNICORE knows the following stage-out protocols:

- ``https://``  : upload a file to an HTTP(s) server (UNICORE will try to *guess* whether the
  HTTP URL refers to a UNICORE server or not)
- ``file://``   : copy file(s) from the job dir to another directory on the remote machine
- ``ftp://``    : upload a file to an FTP server


Specifying credentials for data staging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some data staging protocols supported by UNICORE require credentials such as username and password.

To pass username and password to the server, the syntax is as follows:

.. code:: json

  { 
    "From": "ftp://someserver:25/some/file", 
    "To": "input_data",
    "Credentials": {
      "Username": "myname",
      "Password": "mypassword"
    }
  }

and similarly for exports.

You caan specify Token value for HTTPS data transfers, which will go into
an HTTP "Authorization: Token ..." header

.. code:: json

  { 
    "From": "https://someserver/some/file", 
    "To": "input_data",
    "Credentials": {
      "Token": "some_token"
    }
  }


You may also specify an OAuth Bearer token for HTTPS data transfers,
which will go into an HTTP "Authorization: Bearer ..." header

.. code:: json

  { 
    "From": "https://someserver/some/file", 
    "To": "input_data",
    "Credentials": {
      "BearerToken": "some_token"
    }
  }

You can leave the token value empty, set to "", if the server already has a valid Bearer token by some 
other means (e.g. from the incoming job submission call).

Redirecting standard input
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to have your application or executable read its standard input from a file, you
can use the following
::

  "Stdin": "filename",

then the standard input will come from the file named *filename* in the job working directory.

Resources
~~~~~~~~~

For batch jobs, you will want to control the resources allocated to your job.
If you don't do this, UNICORE will use the default settings configured by the site.


Specifying resources
^^^^^^^^^^^^^^^^^^^^
  
Resources are requested using a ``Resources`` section:

.. code:: json

  {
    "Resources": {

      "Queue" : "fast",  
      "Runtime": "12h",  
      "Nodes": "8"

    }
  }
  

UNICORE has the following built-in resource names:

.. include:: tables/resources.rst


Sites may define additional, *custom* resources, which you can use, too.


Specifying an accounting project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the system you're submitting to requires a project name for accounting purposes, you
can specify the account (or project) you want to charge the job to using the ``Project`` element:
::

  "Project" : "my_project",

(putting the "Project" into the "Resources" element will work, too)

Miscellaneous options
~~~~~~~~~~~~~~~~~~~~~

Umask
^^^^^

The umask controls the permissions of files created by the job and any
processes that are launched from it. UNICORE's default will usually be
"077" if not otherwise conigured. If you want to change the initial umask 
value, you can use the ``Umask`` keyword, e.g.
::

  "Umask": "022",

(the value will interpreted as an octal string)

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


Advanced notification settings (UNICORE 9.2.0 and later)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, UNICORE will send notifications when the job enters ``RUNNING`` state or is done, and
the status changes to ``SUCCESSFUL`` or ``FAILED``.

For special use cases, you may need to use more detailed notification settings, for example when

  - you want notifications on certain low-level (e.g. Slurm level) status changes
  - you want notifications on more or other UNICORE-level status changes.

This advanced notification setup looks like this:

.. code:: json

   {
     "NotificationSettings" : {
       "URL": "https://your-service-url",
       "status": [ "STAGINGOUT", "SUCCESSFUL" ],
       "bssStatus": [ "CONFIGURING" ]
     }
   }

where ``status`` is a list of UNICORE-level status strings, and ``bssStatus``
is a list of BSS-level status strings. If ``status`` is not given explicitly,
the default (RUNNING, SUCCESSFUL, FAILED) are used.

The notifications sent by UNICORE contain the ``href`` job URL, and either
a ``bssStatus`` field, or a ``status``, depending on what triggered the
notification message.


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

