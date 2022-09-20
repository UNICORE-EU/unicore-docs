.. _workflow-manual:

Workflow Service Manual
=======================

The UNICORE Workflow service provides advanced workflow processing
capabilities using UNICORE resources.  The Workflow service provides
graphs of activities including high-level control constructs
(*for-each*, *while*, *if-then-else*, etc), and submits and manages the
execution of single UNICORE jobs.

The Workflow service offers a :ref:`REST API <rest-api>` for workflow
submission and management and uses an easy-to-understand
:ref:`workflow description <workflow-description>` syntax in JSON format.

Thanks to a flexible internal workflow model and execution engine, the
Workflow service can be in principle extended with custom workflow
parsers and custom activities.

The Workflow service supports the full range of authentication options
provided by UNICORE and uses JWT tokens for delegated authentication
when submitting jobs to the execution sites.

For more information about UNICORE visit https://www.unicore.eu.

.. include:: setup.rest

.. include:: config.rest

.. include:: update.rest
