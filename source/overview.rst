.. _unicore-overview:


Overview
********

UNICORE Features
----------------

UNICORE has special characteristics that make it unique among middleware systems. 
The UNICORE design is based on several guiding principles, that serve as key objectives 
for further enhancements. UNICORE deals with authentication, user mapping and authorization, 
and provides a comprehensive set of RESTful APIs for HPC access and workflows.

Services and APIs
~~~~~~~~~~~~~~~~~

    * Batch jobs with pre- and postprocessing
    * Support for common resource managers such as SLURM or LoadLeveler
    * File system access and file transfer
    * Site-to-site file transfer
    * Cross-site workflows featuring graphs, loops, conditions, variables, hold/continue, workflow data management
    * Metadata
    * Service Registry

Security
~~~~~~~~

    * Flexible user authentication: username/password, OpenID Connect, X\.509, ...
    * Flexible user mapping
    * Based on open standards: X\.509 Public Key Infrastructure, TLS, SAML, OIDC, XACML, ...

Clients
~~~~~~~

    * Commandline client: Job execution, data transfer, workflows, scripting, batch mode, extensible
    * Dedicated client for the UFTP high performance file transfer
    * pyUNICORE Python client library

Add-ons
~~~~~~~

    * Standalone UFTP suite for high-performance data transfer (can be used independently of UNICORE)
    * Unity: Identity Management server, SAML compliant, administration GUI, many features, see unity-idm.eu


UNICORE Architecture
--------------------

The architecture of UNICORE is three-layered in client layer, service layer and 
target system layer as shown in the figure below. 

.. image:: _static/unicore-arch.png
  :width: 600
  :alt: UNICORE Architecture
