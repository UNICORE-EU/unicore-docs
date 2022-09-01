.. _ucc-manual:

User Manual
===========

Overview
--------

The **U**\ NICORE **C**\ ommandline **C**\ lient (UCC) is a full-featured client for the 
UNICORE middleware. UCC has client commands for all the UNICORE basic 
services and the :ref:`UNICORE workflow system <workflow>`.

It offers the following functions

 * :ref:`Job submission and management <ucc_jobs>`

 * :ref:`Batch mode <ucc_batch>` job submission and processing with many :ref:`performance tuning <performance-tuning>` options

 * :ref:`Data movement <ucc_datamanagement>` (upload, download, server-to-server copy, etc) using the
   UNICORE storage management functions and available data transfer protocols

 * Storage functions (:ref:`ls_command`, :ref:`mkdir_command`, \.\.\.) including :ref:`creation of storage instances
   <create-storage>` via storage factories

 * Support for UNICORE :ref:`workflow submission and management <ucc_workflow>`

 * Support for the :ref:`UNICORE metadata <ucc_metadata>` system
 
 * Support for :ref:`sharing UNICORE resources <ucc_share>` via ACLs

 * Information about the available services is provided via the :ref:`system-info <system-info>` command

 * Various utilities like a :ref:`shell mode <ucc_shell>`, :ref:`low-level REST API <rest-command>` operations and others

 * Extensibility through custom commands and the possibility to 
   :ref:`run scripts <ucc_scripting>` written in the Groovy programming language

 * :ref:`Built-in help <ucc_help>`

.. note::

 Starting with Version 8 of the UCC, the :ref:`UNICORE REST API <rest-api>` is used
 exclusively for client-server communications.


For more information about UNICORE visit
https://www.unicore.eu.

.. include:: install.rest

.. include:: quickstart.rest

.. include:: options.rest

.. include:: jobs.rest

.. include:: jobdescription.rest

.. include:: datamanagement.rest

.. include:: metadata.rest

.. include:: workflow.rest

.. include:: batch.rest

.. include:: shell.rest

.. include:: share.rest

.. include:: admin.rest

.. include:: scripting.rest

.. include:: faq.rest
