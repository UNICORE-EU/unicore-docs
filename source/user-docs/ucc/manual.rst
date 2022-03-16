.. _ucc-manual:

User Manual
===========

Overview
--------

The UNICORE Commandline client (UCC) is a full-featured client for the 
UNICORE middleware. UCC has client commands for all the UNICORE basic 
services and the UNICORE workflow system.

It offers the following functions

 * Job submission and management

 * Batch mode job submission and processing with many performance tuning options

 * Data movement (upload, download, server-to-server copy, etc) using the
   UNICORE storage management functions and available data transfer protocols

 * Storage functions (``ls``, ``mkdir``, ...) including creation of storage instances
   via storage factories

 * Support for UNICORE workflow submission and management

 * Support for the UNICORE metadata system
 
 * Support for sharing UNICORE resources via ACLs

 * Information about the available services is provided via the ``system-info`` command

 * Various utilities like a *shell* mode, low-level REST API operations and others

 * Extensibility through custom commands and the possibility to run scripts written 
   in the Groovy programming language

 * Built-in help

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
