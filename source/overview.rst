.. _unicore-overview:


Overview
********

`UNICORE <https://www.unicore.eu>`_ (**UN**\ iform **I**\ nterface to 
**CO**\ mputing **RE**\ sources) provides tools and
services for building federated systems, making high-performance
computing and data resources accessible in a seamless and secure way
for a wide variety of applications in intranets and the internet.

.. figure:: _static/unicore-arch.png
   :width: 600
   :alt: UNICORE Architecture
   :align: center
   
   UNICORE Architecture


UNICORE Features
----------------

UNICORE provides a comprehensive set of :ref:`RESTful APIs <rest-api>` for HPC access and workflows,
dealing with user authentication, user account mapping and authorization in a highly flexible way.

Services and APIs
~~~~~~~~~~~~~~~~~

- Batch jobs with pre- and postprocessing
- Support for common resource managers such as SLURM or LSF
- File system access and file transfer
- Site-to-site file transfer
- Cross-site workflows featuring graphs, loops, conditions, variables, hold/continue, workflow 
  data management
- Direct access to applications running on HPC (e.g. for steering or visualisation)
- Metadata
- Service Registry

Security
~~~~~~~~

- Flexible user authentication: username/password, OpenID Connect, SSH keys, X\.509, ...

- Flexible mapping of users to local accounts and groups

- Based on open standards: X\.509 Public Key Infrastructure, TLS, SAML, OIDC, XACML, ...

Clients
~~~~~~~

- :ref:`Commandline client <ucc>`: Job execution, data transfer, workflows, scripting, batch mode, extensible
- Dedicated `client for UFTP
  <https://uftp-docs.readthedocs.io/en/latest/user-docs/uftp-client/>`_ 
  high performance file transfer and data management features
- `pyUNICORE <https://github.com/HumanBrainProject/pyunicore/>`_ Python client library

Add-ons
~~~~~~~

- `Standalone UFTP suite <https://uftp-docs.readthedocs.io/en/latest>`_ for high-performance data transfer 
  (can be used independently of UNICORE)
- `Unity Identity Management system <https://unity-idm.eu>`_, supports LDAP, OAuth, SAML, 
  federated AAI and a lot more

