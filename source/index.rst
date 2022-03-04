.. _unicore-docs:


UNICORE Documentation
=====================

`UNICORE <https://www.unicore.eu>`_ (**U**\ niform **I**\ nterface to **CO**\ mputing 
**RE**\ sources) offers a ready-to-run system including client and server software. 
It makes distributed computing and data resources available in a seamless and secure way 
in intranets and the internet. 

.. image:: _static/unicore-features.png
   :width: 600
   :alt: UNICORE Features 


* :ref:`unicore-overview` gives an overview of the UNICORE features and the UNICORE architecture. 
  
.. toctree::
	:maxdepth: 2
	:caption: UNICORE Documentation
	:hidden:

	overview


User Documentation
==================

* :ref:`ucc` - a full featured commandline client for UNICORE.
* :ref:`rest-api` - REST-API for job submission and management, 
  data access and transfer, workflow submission and management

  * :ref:`job-description` - the job description format 
  * :ref:`workflow-description` - the workflow description language 

.. toctree::
	:maxdepth: 2
	:caption: User Documentation
	:hidden:

	ucc/index
	rest-api/index
	rest-api/job-description/index
	rest-api/workflow-description/index


Administrator documentation
===========================

* :ref:`gateway` - an optional server component that
  provides a reverse https proxy, allowing you to run several backend
  servers (:ref:`unicorex`, :ref:`Registery <registry>`, ...) behind a single   address.
  
* :ref:`unicorex` - the central server component of a typical UNICORE  installation
  that provides REST APIs for job management and data access  services for a
  single compute cluster (or just a file system).

* :ref:`tsi` - the Target System Interface (TSI) server is used to 
  interface to a resource manager such as Slurm and to access files 
  on the cluster.
  
* :ref:`xuudb` - an optional service, that is best
  suited as a per-site service, providing attributes for multiple
  UNICORE/X-like services at a site. The XUUDB maps a UNICORE user identity 
  (which is formally an X.500 distinguished name (DN)) to a set of attributes 
  which are typically used to provide local account details (uid, gid(s)) and
  commonly also to provide authorization information, i.e. the
  user's role.

* :ref:`workflow` - provides advanced workflow processing
  capabilities using UNICORE resources.  The Workflow service provides
  graphs of activities including high-level control constructs
  (for-each, while, if-then-else, etc), and submits and manages the
  execution of single UNICORE jobs.
  
* :ref:`registry` - the Registry server is a specially configured
  UNICORE/X server which provides the information about available
  services to clients and other services. 

* `UFTPD <https://uftp-docs.readthedocs.io/en/latest/uftpd/index.html#uftpd>`_ - 
  the UNICORE File Transfer Server for high performance data transfer


.. toctree::
	:maxdepth: 2
	:caption: Administrator Documentation
	:hidden:
	
	gateway/index
	unicorex/index
	tsi/index
	xuudb/index
	workflow/index
	unicorex/registry


Getting Support
===============

For more information, please see the :ref:`links` and :ref:`support` page.


.. toctree::
	:caption: Getting Support
	:hidden:
	
	links.rst
	support

License
=======

UNICORE is available under the :ref:`BSD 2-Clause License <license>`.

.. toctree::
	:caption: LICENSE
	:hidden:
	
	license


Indices and tables
******************

* :ref:`genindex`
* :ref:`search`


Last updated: |today|
