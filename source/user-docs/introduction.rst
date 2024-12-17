.. _introduction:

|user-guide| Introduction
*************************

.. |user-guide| image:: ../_static/user-guide.png
	:height: 32px
	:align: middle

This document gives an introduction for new UNICORE users - what can UNICORE do for you?


Why use UNICORE?
----------------

The main functionality offered by UNICORE is a secure and flexible programmatic
access to HPC compute and storage.

You can use UNICORE for all those tasks where the "usual" SSH access is not flexible
or not secure enough:

 - automation tasks
 - multi-step and even multi-site workflows
 - hybrid cloud/HPC applications
 - integration into third party (web) applications

What client should you use?
---------------------------

For most of the common end-user tasks, like interactive use, scripting,
automation etc, the :ref:`UNICORE Commandline client <ucc>` will be the
most convenient. It provides a fully-fledged commandline tool.

For integration into third party applications, we provide a Python library
`PyUNICORE <https://pyunicore.readthedocs.io/>`_.

If you are not using Python (or Java), you can always directly use the 
:ref:`REST API <rest-api>`.

Use case: job execution
-----------------------

Running jobs is the backbones of UNICORE - you can use it as a fancy job submission
and job monitoring tool, or simply as a "replacement" for SSH.


Executing commands via UNICORE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To simply run a command on a login node of the HPC cluster,
you can use the ``ucc exec`` command

.. code:: console

  ucc exec -- whoami

This will run the command and get standard output and error back to the client and display them.

For more complex cases, you can create a JSON job description and run that via UCC.

.. code:: json

  {
    "Job type": "ON_LOGIN_NODE",
    "Executable": "/bin/bash ./myscript.sh",
    "Imports": [
      {
        "From": "inline://dummy", "To": "myscript.sh",
        "Data": [
          "whoami",
          "hostname",
          "date"
        ]
      }
    ]
  }

which you can then run via  ``ucc run`` (see the section :ref:`ucc_jobs` for more details).

For simplicity, this example puts the script directly in the job via an "inline"
data transfer. There's a number of other options available to deal with file transfers (see 
`Job data management <./rest-api/job-description/index.html#job-data-management>`_).


Running batch jobs
~~~~~~~~~~~~~~~~~~

The most common use case on a HPC system is the batch job - your job gets submitted to
the cluster's queueing system (e.g. Slurm), and is executed whenever the required resources
become available.

You as the user need to provide the required resources - which queue,
how long do you need the job to run, how many nodes etc, as well as the command to execute.

For example to run 4 instances of "date" on one node of a cluster, the job would look
like this:

.. code:: json

  {
    "Executable": "srun -ntasks=4 date",
    "Resources": {
      "Nodes": 1,
      "Runtime": 30
    }
  }

Running this job via ``ucc run`` will submit and monitor the job, waiting for its completion and
then download the standard output and error files (see :ref:`ucc_batch` for more details). UCC has many options to modify this behaviour,
and you will often submit the job without waiting for it to finish (see the section  
`Options overview <./ucc/manual.html#options-overview>`_).

The ``ucc list-jobs`` command is used to list all your jobs (that were submitted via UNICORE),
and you can use other ucc commands to interact with the job or download results.

Advanced batch jobs
~~~~~~~~~~~~~~~~~~~

If you prefer to use a more low level way to allocate resources, you can provide a file
containing resource requests, e.g. for Slurm, and tell UNICORE to use that via special
"Job type" and "BSS file" elements in your job:

.. code:: json

  {
    "Job type": "RAW",
    "BSS file": "sbatch.request",

    "Executable": "srun -ntasks=4 date",

    "Imports": [
      {
        "From": "inline://dummy", "To": "sbatch.request",
        "Data": [
          "#!/bin/bash",
          "#SBATCH --account=yourproject",
          "#SBATCH --nodes=1",
          "#SBATCH --output=stdout",
          "#SBATCH --error=stderr",
        ] 
      }
    ]
  }

For simplicity, this example contains the script directly in the job description
via an "inline" data transfer.

Note that this only needs to contain resource requests, the actual execution part will be document
by UNICORE. UNICORE will then track this batch job as usual.
