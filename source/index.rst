.. _unicore-docs:

UNICORE Documentation
*********************

`UNICORE <https://www.unicore.eu>`_ (**U**\ niform **I**\ nterface to **CO**\ mputing **RE**\ sources) a software suite 
for building federated systems, providing secure and seamless access to heterogeneous resource such as compute clusters 
and file systems. UNICORE deals with authentication, user mapping and authorization, and provides a comprehensive set 
of RESTful APIs for HPC access and workflows.

UNICORE offers a ready-to-run system including client and server software. It makes distributed computing and data 
resources available in a seamless and secure way in intranets and the internet.

UNICORE has special characteristics that make it unique among middleware systems. The UNICORE design is based on 
several guiding principles, that serve as key objectives for further enhancements.

.. image:: _static/unicore-features.png
  :width: 600
  :alt: UNICORE Features 

UNICORE Components
~~~~~~~~~~~~~~~~~~

The UNICORE software system contains the following components:

* :ref:`unicorex` - the central server component of a typical UNICORE  installation
  that provides REST APIs for job management and data access  services for a
  single compute cluster (or just a file system).

* :ref:`gateway` - an optional server component that
  provides a reverse https proxy, allowing you to run several backend
  servers (:ref:`unicorex`, :ref:`Registery <registry>`, ...) behind a single   address.

* :ref:`tsi` - the Target System Interface (TSI) server is used to 
  interface to a resource manager such as Slurm and to access files 
  on the cluster.

* :ref:`workflow` - provides advanced workflow processing
  capabilities using UNICORE resources.  The Workflow service provides
  graphs of activities including high-level control constructs
  (for-each, while, if-then-else, etc), and submits and manages the
  execution of single UNICORE jobs.

* :ref:`xuudb` - an optional service, that is best
  suited as a per-site service, providing attributes for multiple
  UNICORE/X-like services at a site. The XUUDB maps a UNICORE user identity 
  (which is formally an X.500 distinguished name (DN)) to a set of attributes 
  which are typically used to provide local account details (uid, gid(s)) and
  commonly also to provide authorization information, i.e. the
  user's role.


* `UFTPD <https://uftp-docs.readthedocs.io/en/latest/uftpd/index.html#uftpd>`_ - the UNICORE File 
  Transfer Server for high performance data transfer

* :ref:`ucc` - a full featured commandline client for UNICORE.


.. image:: _static/unicore-arch.png
  :width: 600
  :alt: UNICORE Architecture 


UNICORE Features
~~~~~~~~~~~~~~~~

.. topic:: Services and APIs

    * Batch jobs with pre- and postprocessing
    * Support for common resource managers such as SLURM or LoadLeveler
    * File system access and file transfer
    * Site-to-site file transfer
    * Cross-site workflows featuring graphs, loops, conditions, variables, hold/continue, workflow data management
    * Metadata
    * Service Registry

.. topic:: Security

    * Flexible user authentication: username/password, OpenID Connect, X\.509, ...
    * Flexible user mapping
    * Based on open standards: X\.509 Public Key Infrastructure, TLS, SAML, OIDC, XACML, ...

.. topic:: Clients

    * Commandline client: Job execution, data transfer, workflows, scripting, batch mode, extensible
    * Dedicated client for the UFTP high performance file transfer
    * pyUNICORE Python client library

.. topic:: Add-ons

    * Standalone UFTP suite for high-performance data transfer (can be used independently of UNICORE)
    * Unity: Identity Management server, SAML compliant, administration GUI, many features, see unity-idm.eu



Getting Support
~~~~~~~~~~~~~~~

For more information, please see the :ref:`support` page.


.. toctree::
	:maxdepth: 2
	:caption: UNICORE Documentation
	:hidden:

	unicorex/index
	gateway/index
	tsi/index
	workflow/index
	xuudb/index
	ucc/index
	
.. raw:: html

   	<hr>

.. toctree::
	:hidden:
	
	links.rst
	faq.rst
	wiki
	support
	license
   
	
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`search`


Last updated: |today|
