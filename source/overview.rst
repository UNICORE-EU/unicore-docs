.. _unicore-overview:


Overview
********

UNICORE (UNiform Interface to COmputing REsources) provides tools and
services for building federated systems, making high-performance
computing and data resources accessible in a seamless and secure way
for a wide variety of applications in intranets and the internet.

UNICORE Architecture
--------------------

The architecture of UNICORE is three-layered in client layer, service layer and 
target system layer as shown in the figure below. 

.. image:: _static/unicore-arch.png
   :width: 600
   :alt: UNICORE Architecture



UNICORE Components
------------------

* :ref:`gateway` - an optional server component that
  provides a reverse https proxy, allowing you to run several backend
  servers (:ref:`unicorex`, :ref:`Registery <registry>`, ...) behind a single address.
  
* :ref:`unicorex` - the central server component of a typical UNICORE  installation
  that provides REST APIs for job management and data access  services for a
  single compute cluster (or just a file system).

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

.. image:: _static/unicore-components.png
  :width: 600
  :alt: UNICORE Components
  

UNICORE Features
----------------

UNICORE has special characteristics that make it unique among middleware systems. 
UNICORE deals with authentication, user mapping and authorization, 
and provides a comprehensive set of :ref:`RESTful APIs <rest-api>` for HPC access and workflows.
The UNICORE design is based on several guiding principles, that serve as key objectives 
for further enhancements. 

Services and APIs
~~~~~~~~~~~~~~~~~

    * Batch jobs with pre- and postprocessing
    * Support for common resource managers such as SLURM or LoadLeveler
    * File system access and file transfer
    * Site-to-site file transfer
    * Cross-site workflows featuring graphs, loops, conditions, variables, hold/continue, workflow 
      data management
    * Metadata
    * Service Registry

Security
~~~~~~~~

    * Flexible user authentication: username/password, OpenID Connect, X\.509, ...
    * Flexible mapping of users to local accounts and groups
    * Based on open standards: X\.509 Public Key Infrastructure, TLS, SAML, OIDC, XACML, ...

Clients
~~~~~~~

    * :ref:`Commandline client <ucc>`: Job execution, data transfer, workflows, scripting, batch mode, extensible
    * Dedicated `client for the UFTP 
      <https://uftp-docs.readthedocs.io/en/latest/user-docs/uftp-client/>`_ 
      high performance file transfer 
    * `pyUNICORE <https://github.com/HumanBrainProject/pyunicore/>`_ Python client library

Add-ons
~~~~~~~

    * `Standalone UFTP suite <https://uftp-docs.readthedocs.io/en/latest>`_ for high-performance data transfer 
      (can be used independently of UNICORE)
    * `Unity Identity Management system <https://unity-idm.eu>`_, supports LDAP, OAuth, SAML, 
      federated AAI and a lot more

