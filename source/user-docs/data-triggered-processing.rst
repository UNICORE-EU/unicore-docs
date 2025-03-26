.. _data-triggered:

|data-triggered-img| Data-triggered processing
**********************************************

.. |data-triggered-img| image:: ../_static/move-files.png
	:height: 32px
	:align: middle

This document describes UNICORE's data-triggered, rule-oriented processing feature.


What is data-triggered processing?
----------------------------------

UNICORE can be set up to automatically scan storages and trigger processing
steps (e.g. submit batch jobs or run processing tasks) according to 
user-defined rules.

This style of processing is storage-oriented, i.e. is defined by the properties
of a UNICORE storage endpoint, and by files accessible on that storage endpoint.

Setting up data-triggered processing
------------------------------------

Depending on the server configuration, data triggered processing is probably disabled 
on the standard storages (HOME, ROOT, etc).

If the UNICORE server provides a "storage factory" service, you can create
an endpoint with data-triggered processing enabled, and you can select the path

For example using UCC:

.. code:: console

  ucc create-storage path=/path/to/your/directory enableTrigger=true


Controlling the scanning process
--------------------------------

To control which directories should be scanned, a file named ``.UNICORE_Rules``
at the top-level of the storage is read and evaluated. This file can be (and 
usually will be) edited and uploaded by the user. It can be modified at any time.


The file is expected to be in JSON format, and has the following elements:

.. code:: json

 {
  "DirectoryScan": {
  
    "IncludeDirs": [
        "project.*"
    ],
    "ExcludeDirs": [
        "project42"
    ],
    "Interval": "30"
  
  },
  
  "Rules": [ ],

  "Enabled": "true | false",

  "Logging": "true | false"

 }


The ``IncludeDirs`` and ``ExcludeDirs`` are lists of Java regular expression strings that denote 
directories (as always relative to the storage root) that should be included or excluded from
the scan.

The optional ``Interval`` element allows you to control the scan interval. A numerical value (seconds),
or a time value with unit such as "1h" can be used here.

The optional ``Enabled`` element allows you to (temporarily) disable the processing,
if you wish.

The optional ``Logging`` element allows you to disable the writing of log files.
Logging is enabled by default, see below. Log files will be written to a directory
``.UNICORE_data_processing`` in the base directory of the storage endpoint.


The ``Rules`` section controls which files are to be processed, and what is to 
be done (actions). This is described below.


Rules
~~~~~

The ``Rules`` section in the ``.UNICORE_Rules`` file is a list
of file match specifications together with a definition of
an *action*, i.e. what should be done for those files that match.

The general syntax is:

.. code:: json

 {
   "DirectoryScan": {
     "IncludeDirs": [ ],
     "ExcludeDirs": [ ]
   },
  
   "Rules": [
     {
       "Name": "example",
       "Match": ".*incoming/file_.*",
       "Action": {  }
     }
   ]
 }

The mandatory elements are:

* ``Name`` : the name of the rule. This is useful when checking the logfiles.

* ``Match`` : a regular expression defining which file paths (relative to 
  storage root) should be processed.

* ``Action`` : the action to be taken.

Variables
^^^^^^^^^

The following variables can be used in the ``Action`` description:

* ``UC_BASE_DIR`` : the storage root directory

* ``UC_CURRENT_DIR`` : the absolute path to the parent directory of the current file 

* ``UC_FILE_PATH`` : the full path to the current file

* ``UC_FILE_NAME`` : the file name

* ``UC_FILES``     : (batched actions only) all the newly detected files, relative to the base directory

Job action
^^^^^^^^^^

This type of action will be executed for a single new file, and
defines a UNICORE job in the usual :ref:`job description syntax <job-description>`.

.. code::

  "Action":
  {
    "Job": { ... }
  }

The ``Job`` element contains a UNICORE job in the
usual :ref:`job description syntax <job-description>`.


Batched job action
^^^^^^^^^^^^^^^^^^

This type of action will be executed for a whole set of newly detected files.

.. code::

  "Action":
  {
    "BatchedJob": { ... }
  }

The ``BatchedJob`` element contains a UNICORE job in the
usual :ref:`job description syntax <job-description>`.

Metadata extraction
^^^^^^^^^^^^^^^^^^^

.. code::

  "Action":
  {
    "Extract": { ... }
  }

This action will extract metadata from all the newly detected files.
The contents of the ``Extract`` element are currently unused.

Sending notifications
^^^^^^^^^^^^^^^^^^^^^

.. code::

  "Action":
  {
    "Notification": "https://url-to-notification-receiver"
  }

This action will send out a HTTP POST request in JSON format to the specified URL.
The JSON will contain information about the new files, as well as the base directory
that is being watched.

An example notification could look like this:

.. code:: json

  {
    "href": "https://unicorex-server-url/rest/core",
    "directory": "/path/to/watched/directory",
    "files": [
      "/path-to-new-file1",
      "/path-to-new-file2"
    ]
  }

(File paths are relative to the base directory!)

Logging
~~~~~~~

If new files are detected, and rules are executed, the server will write a short log file
to a directory ".UNICORE_data_processing".

Stopping the processing
-----------------------

Since data-triggered processing is tied to the storage instance, you can stop
it by sending an empty REST POST to an URL on the storage, e.g. 

.. code:: console

  ucc rest post "{}" 'storage-URL'/actions/stop-processing

Destroying the storage instance will also stop the processing
(but not delete any files).

.. code:: console

  ucc rest delete "{}" 'storage-URL'

Example
-------

As an example, we setup a task that generates checksums for all new files
that are detected in the `incoming` directory.

The ``.UNICORE_Rules`` file could look like this:

.. code:: json

  {
    "DirectoryScan": {
      "IncludeDirs": [
         "incoming"
      ],
  },

    "Rules": [ 
      {
        "Name": "generate-hash",
        "Match": ".*",
        "Action": { 
           "Job": { 
              "Executable": "sha256sum ${UC_FILE_PATH}",
              "Exports": [ 
                { 
                  "From": "stdout", 
                  "To": "file://${UC_BASE_DIR}/checksums/${UC_FILE_NAME}.sha"
                }
              ]
            }
        }
      }
    ]
  }


.. raw:: html

   <hr>
