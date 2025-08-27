.. _unicore-howto-testmachine:


|user-guide| Installing UNICORE for Testing
*******************************************

.. |user-guide| image:: _static/user-guide.png
   :height: 32px
   :align: middle

|overview-img| Overview
-----------------------

.. |overview-img| image:: _static/overview.png
   :height: 32px
   :align: middle

This How-To explains how to quickly set up UNICORE servers on a single
test machine or even on your laptop.


|checklist-img| Prerequisites
-----------------------------

.. |checklist-img| image:: _static/checklist.png
   :height: 32px
   :align: middle

- Java 11 or later (OpenJDK or Oracle Java recommended)
- Python 3.x (required for TSI and installation scripts)

.. important::
   **Security Notes**

   UNICORE servers (except TSI) use X.509 certificates and
   client-authenticated SSL. The bundle includes demo certificates
   and allows creating self-signed ones.

   - Never use demo certificates in production!  
   - For production, use proper CA-signed SSL certificates.  
   - Run servers as a dedicated non-root user (except TSI).  
     See the Installation section for details.


|config-img| Installation and Configuration
-------------------------------------------

.. |config-img| image:: _static/configuration.png
   :height: 32px
   :align: middle

Run all servers as a dedicated non-root user (e.g., ``unicore``).  
Do **not** start servers (except TSI) as ``root``.

**Install the bundle**

Download either the ``.tgz`` archive or the Debian package (``.deb``)
from the `Core Server Bundle <https://github.com/UNICORE-EU/server-bundle/releases>`_.

For ``.tgz`` files, unpack with:

.. code:: console

   $ tar xzf unicore-server-bundle-<version>.tgz

For Debian packages, install with:

.. code:: console

   $ sudo dpkg -i unicore-server-bundle-<version>.deb

The bundle includes the following components:

- Gateway
- UNICORE/X
- TSI
- Registry (only needed for multi-site workflows)
- Workflow (only needed for multi-site workflows)
- XUUDB (optional; provides user attribute management)

A typical setup installs Gateway and UNICORE/X on a VM or server,  
and TSI on the login node of a compute cluster.

**Configure and install**

The bundle provides helper scripts and a configuration file
(``configure.properties``). In most cases, defaults work, but edit the
file if you need to adjust settings such as ports, hostnames, etc.

Steps:

1. Edit ``configure.properties`` (optional, if you need to adjust settings)
2. Run:

   .. code:: console

      ./configure.py [<unicore_user>] [<hostname>]

   - ``<unicore_user>``: UNIX account to run the servers (default: current user)  
   - ``<hostname>``: target host (default: localhost)

3. Run:

   .. code:: console

      ./install.py

4. Install TSI separately on the cluster login node.

The ``configure.py`` script updates component configuration files and keeps
backups as ``*_origin``, so it can be safely re-run.

**Multi-host deployment**

1. Create the same UNIX user (e.g., ``unicore``) on each host.  
2. Decide which component runs on which host; note hostnames and ports.  
3. Copy the bundle to each machine.  
4. Maintain a master ``configure.properties`` file with all host/port settings.  
5. On each host, edit the config file to select the components to install, then run the installer.

.. note::
   If you re-run ``configure.py`` after starting servers, clean up old
   data first:

   .. code:: console

      rm -f unicorex/data/*
      rm -f registry/data/*
      rm -f workflow/data/*

   Re-configuration uses the ``*_origin`` backup files as templates.


Starting UNICORE
================

Start the UNICORE servers using the ``start.sh`` script in the
installation directory. 

Testing Installation
----------------------

To check that authentication and user mapping work correctly, run:

.. code:: console

   export BASE=https://unicore-host:8080/TEST/rest/core
   # Replace `unicore-host` with your server host (e.g., localhost)
   curl -k -u demouser:test123 -H "Accept: application/json" \
       $BASE?fields=client | python3 -m json.tool

Expected output:

.. code:: console

   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
   100   215  100   215    0     0    676      0 --:--:-- --:--:-- --:--:--   678
   {
       "client": {
           "role": {
               "selected": "user",
               "availableRoles": [
                   "user"
               ]
           },
           "authenticationMethod": "PASSWORD_FILE",
           "dn": "CN=Demo User, O=UNICORE, C=EU",
           "xlogin": {
               "UID": "unicore",
               "availableGroups": [],
               "availableUIDs": [
                   "unicore"
               ]
           }
       }
   }

.. note::
   If needed, servers can be stopped using the ``stop.sh`` script in the same directory.
   
   
|support_img| Reporting bugs
----------------------------

.. |support_img| image:: _static/support.png
   :height: 32px
   :align: middle

Report issues via:

- GitHub Issues: https://github.com/UNICORE-EU/server-bundle/issues  
- Website: https://www.unicore.eu  
- GitHub Org: https://github.com/UNICORE-EU  
- Twitter: https://twitter.com/UNICORE_EU  
- Email: unicore-support@lists.sf.net


.. raw:: html

   <hr>