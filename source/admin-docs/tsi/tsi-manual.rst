.. _tsi-manual:

|user-guide-img| TSI Manual
===========================

.. |user-guide-img| image:: ../../_static/user-guide.png
	:height: 32px
	:align: middle

The TSI performs the work on behalf of UNICORE users and so must be
able to execute processes under different uids and gids. Therefore, in
production it must be run with sufficient privileges to allow this
(during development and testing it can be run as a normal user).

You can configure the TSI and :ref:`UNICORE/X <unicorex>` to communicate via SSL. In
this case, you need a server certificate for the TSI. For details, see
section :ref:`tsi_ssl`.

The TSI is one point where UNICORE's seamless model meets local
variations and so will usually need to be adapted to the target
system. This is described in section :ref:`tsi_localization`.

.. note:: 
  In production environments, the TSI will run with elevated privileges.
  Make sure to read and understand section :ref:`tsi_security` on security and hardening 
  the system.


|checklist-img| Prerequisites
-----------------------------

.. |checklist-img| image:: ../../_static/checklist.png
	:height: 32px
	:align: middle

The TSI requires Python Version 3.6 or later. It works only on
Unix-style operating systems (e.g. Linux or Mac OS/X), Windows is not
directly supported.

The TSI uses the ``setpriv`` tool to run as a non-root user (*unicore*)
with the capability to switch uid/gid to the requested values, in
order to perform tasks on behalf of the requesting user.
If this is not available on the system, the TSI will run
as *root* (but never perform any actions as *root*).

Batch system status checks (e.g. via ``squeue`` for Slurm) will be
executed under a system account (usually *unicore*) which is
configured in the UNICORE/X server configuration. Note that this
system account cannot be *root*, as the TSI will never execute
anything as *root*.

The system account **MUST** be able to list batch job status from all
users! If necessary, configure your batch system accordingly. For
details on this procedure we refer to the documentation of your batch
system.

If you want to run user scripts in the proper user slice, you can
enable PAM, which requires an appropriate PAM module file, by 
default this is called ``unicore-tsi``.


|install-img| Installation
--------------------------

.. |install-img| image:: ../../_static/installer.png
	:height: 32px
	:align: middle

The TSI is available either as part of the
`UNICORE core server <https://github.com/UNICORE-EU/server-bundle/releases>`_ bundle package, 
or `separately <https://github.com/UNICORE-EU/tsi/releases>`_


Batch system specific distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the installation tools of your operating system to install the
package. The following table shows the location of the TSI files.

.. table::
 :widths: 25 40 35
 :class: tight-table
 
 +---------------------+-----------------------------+---------------------+
 | Name in this manual | Location                    | Description         |
 +=====================+=============================+=====================+
 | CONF                | /etc/unicore/tsi            | Configuration files |
 +---------------------+-----------------------------+---------------------+
 | BIN                 | /usr/share/unicore/tsi/bin  | Start/stop scripts  |
 +---------------------+-----------------------------+---------------------+
 | LIB                 | /usr/share/unicore/tsi/lib  | Python files        |
 +---------------------+-----------------------------+---------------------+
 | LOGS                | /var/run/unicore/tsi/logs   | Log files           |
 +---------------------+-----------------------------+---------------------+


Generic distribution
~~~~~~~~~~~~~~~~~~~~

The generic TSI distribution contains several TSI variations for many 
popular batch systems.

Before being able to use the TSI, you must install one of the TSI variants 
and configure it for your local environment:

- Execute the installation script ``Install.sh`` and follow the instructions 
  to copy all required files into a new TSI installation directory.

- Adapt the configuration as described below.

In the following, ``TSI_INSTALL`` refers to the directory where you installed the 
TSI. This has the following sub-directories:

.. table::
 :widths: 25 25 50
 :class: tight-table
 
 +---------------------+--------------------+--------------------------------------+
 | Name in this manual | Location           | Description                          |
 +=====================+====================+======================================+
 | TSI_INSTALL         |                    | Base directory chosen during         |
 |                     |                    | execution of ``Install.sh``          |
 +---------------------+--------------------+--------------------------------------+
 | CONF                | TSI_INSTALL/conf   | Configuration files                  |
 +---------------------+--------------------+--------------------------------------+
 | BIN                 | TSI_INSTALL/bin    | Start/stop scripts                   |
 +---------------------+--------------------+--------------------------------------+
 | LIB                 | TSI_INSTALL/lib    | Python files                         |
 +---------------------+--------------------+--------------------------------------+
 | LOGS                | TSI_INSTALL/logs   | Log files                            |
 +---------------------+--------------------+--------------------------------------+


.. _tsi_permissions:

File permissions
~~~~~~~~~~~~~~~~

The permissions on the TSI files should be set to **read only for the
owner**. The default installation procedure will initially take care of
this. As the TSI is executed with elevated privileges, you should
never leave any TSI files (or directories) writable after any update.

|config-img| Configuring the TSI
--------------------------------

.. |config-img| image:: ../../_static/configuration.png
	:height: 32px
	:align: middle

The TSI is configured by editing the :file:`{CONF}/tsi.properties` and 
:file:`{CONF}/startup.properties` files. Please review these two files 
carefully.

Changes outside the config files should not be necessary, except for
new portings and any local adaptations, as detailed in the next
section.  If changes are made, they should be passed on to the
UNICORE developers, so that they can be incorporated into future
releases of the scripts. To do that, send mail to
`unicore-support <mailto:unicore-support@lists.sf.net>`_ or use the `issue 
tracker <https://sourceforge.net/p/unicore/issues>`_ at sourceforge.

Verifying
~~~~~~~~~

Before starting the TSI, you should make sure that the batch system integration
is working correctly. See the section on :ref:`tsi_localization` below!

TSI networking configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In tsi.properties, the TSI host interface and port are defined, as well 
as the allowed UNICORE/X host(s).
::

  # TSI host interface, use "0.0.0.0" to bind to all interfaces
  tsi.my_addr=localhost

  # The port on which the TSI will listen for UNICORE/X requests
  tsi.my_port=14433

  # Comma-separated list of UNICORE/X machine(s) from where
  # connections are allowed
  tsi.unicorex_machine=my-unicorex-a.server.org, my-unicorex-b.server.org

  # Optionally, define a fixed callback port to UNICORE/X
  # (If not set, the TSI will use the port requested by UNICORE/X)
  tsi.unicorex_port=7654


NOTE: if using SSL (see section :ref:`tsi_ssl`), the ``tsi.unicorex_machine``
is ignored.


You can optionally configure a range of local ports for the TSI to use.
If this is set, the TSI will use free ports from that range only. Per UNICORE/X
connection, two local ports are required, so make sure to not set this range
too small (should be at least 20 ports).
::

   tsi.local_portrange=50000:50100


UNICORE/X configuration
~~~~~~~~~~~~~~~~~~~~~~~~

UNICORE/X configuration is described fully in the relevant :ref:`UNICORE/X manual
<unicorex-manual>`. Here we just give the most important steps to get the TSI up 
and running.

The relevant UNICORE/X config file is usually called ``tsi.config``.

Hostnames and ports
^^^^^^^^^^^^^^^^^^^

UNICORE/X needs to know the TSI hostname and port::

  CLASSICTSI.machine=frontend.mycluster.org
  CLASSICTSI.port=4433


SSL support
^^^^^^^^^^^

If you wish to setup SSL for the UNICORE/X-to-TSI communication,
please refer to section :ref:`tsi_ssl`.


ACL support
~~~~~~~~~~~

The TSI (together with UNICORE/X) provides a possibility to manipulate
file **A**\ ccess **C**\ ontrol **L**\ ists (ACLs). To use ACLs, the appropriate 
support must be available from the underlying file system. Currently, only the
so called POSIX ACLs are supported (*so called* as in fact the
relevant documents POSIX 1003.1e/1003.2c were never finalized), using
the popular ``setfacl`` and ``getfacl`` commands. Most current file
systems provide support for the POSIX ACLs.

.. note::
  Note, that the current version is relying on extensions of the ACL
  commands which are present in the Linux implementation. In case of
  other implementation (e.g. BSD) the ACL module should be extended,
  otherwise the default ACLs (which are used for directories) support
  will not work.

To enable POSIX ACL support you typically must ensure that:

- the required file systems are mounted with ACL support turned on,

- the ``getfacl`` and ``setfacl`` commands are available on your machine.

Configuration of ACLs is performed in the ``tsi.properties`` file. First of all, you can define
a location of ``setfacl`` and ``getfacl`` programs with ``tsi.setfacl`` and ``tsi.getfacl`` 
properties. By providing absolute paths you can use non-standard locations, typically it is 
enough to leave the default, non-absolute values which will use programs as available under the 
standard shell search path. Note that if you will comment any of those properties, the POSIX 
ACL subsystem will be turned off.

Configuration of ACL support is per directory, using properties of the format: 
``tsi.acl.PATH``, where *PATH* is an absolute directory path for which the setting is being made. 
You can provide as many settings as required, the most specific one will be used. 
The valid values are ``POSIX`` and ``NONE`` respectively for POSIX ACLs and for turning 
off the ACL support. 

Consider an example::

  tsi.acl./=NONE
  tsi.acl./home=POSIX
  tsi.acl./mnt/apps=POSIX
  tsi.acl./mnt/apps/external=NONE

The above configuration turns off ACL for all directories, except for
everything under ``/home`` and everything under ``/mnt/apps`` with the
exception of ``/mnt/apps/external``.

.. warning::
  Do not use symbolic links or ``..`` or ``.`` in properties configuring
  directories - use only absolute, normalized paths. Currently spaces in
  paths are also unsupported.


.. note::
 The ACL support settings are typically cached on the UNICORE/X side (for a few minutes). 
 Therefore, after changing the TSI configuration (and after resetting the TSI) you have to 
 wait a bit until the new configuration is applied also in UNICORE/X.


ACL limitations
^^^^^^^^^^^^^^^
There is no ubiquitous standard for file ACLs. *POSIX draft* ACLs are by far the most popular 
however there are several other implementations. Here is a short list that should help to figure out
the situation:

- POSIX ACLs are supported on Linux and BSD systems.

- The following file systems support POSIX ACLs: Lustre, ext{2,3,4}, JFS, ReiserFS and XFS.

- Solaris ACLs are very similar to POSIX ACLs and it should be possible to use TSI to manipulate them 
  at least partially (remove all ACL operation won't work for sure and note that usage of 
  Solaris ACLs was never tested). Full support may be provided on request.

- NFS version 4 provides a completely different, and currently unsupported implementation of ACLs.

- NFS version 3 uses ACLs with the same syntax as Solaris OS.

- There are also other implementations, present on AIX or Mac OS systems or in AFS FS.

Note that in future more ACL types may be supported and will be configured in the same manner, just using
a different property value. 

.. _tsi_ssl:

Enabling SSL for the UNICORE/X - TSI communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SSL support should be enabled for the UNICORE/X - TSI communication to
increase security. This is a **MUST** when UNICORE/X and TSI run on the
same host, and/or user login is possible on the UNICORE/X host, to
prevent attackers gaining control over the TSI.

You need:

- a private key and certificate for the TSI,

- the CA certificate of the TSI certificate,

- the DN (subject distinguished name) of the UNICORE/X servers that 
  shall be allowed to connect to the TSI,

- the CA certificate of the UNICORE/X certificate.

The certificate of the TSI signer CA must be added to the UNICORE/X 
truststore.

The following configuration options must be set in ``tsi.properties``:

:``tsi.keystore``: file containing the private TSI key in PEM format

:``tsi.keypass``: password for decrypting the key

:``tsi.certificate``: file containing the TSI certificate in PEM format

:``tsi.truststore``: file containing the certificate of the accepted CA(s) 
 in PEM format

:``tsi.allowed_dn.NNN``: allowed DNs of UNICORE/X servers in RFC format

SSL is activated if the keystore file is specified in ``tsi.properties``.

The truststore file contains the CA cert(s)::

  -----BEGIN CERTIFICATE-----

    ... PEM data omitted ...	
  
  -----END CERTIFICATE-----
  -----BEGIN CERTIFICATE-----
  
    ... PEM data omitted ...
  	
  -----END CERTIFICATE-----


The ``tsi.allowed_dn.NNN`` properties are used to specify which certificates are allowed, 
for example,
::

  tsi.allowed_dn.1=CN=UNICORE/X 1, O=UNICORE, C=EU
  tsi.allowed_dn.2=CN=UNICORE/X 2, O=UNICORE, C=EU


.. attention:: 
  If you do not specify any access control entries, all 
  certificates issued by trusted CAs are allowed to
  connect to the TSI. Be very careful to prevent
  illicit access to the TSI!


When UNICORE/X connects, its certificate is checked:

- the UNICORE/X cert has to be valid (i.e. issued by a trusted CA and 
  not expired),

- the subject of the UNICORE/X cert is checked against the configured ACL 
  (list of allowed DNs).

On the UNICORE/X side, set the following property (usually in 
the ``xnjs.properties`` file)::

  # enable SSL using the UNICORE/X key and trusted certificates
  CLASSICTSI.ssl.disable=false


.. _tsi_localization:

|settings-img| Adapting the TSI to your system
----------------------------------------------

.. |settings-img| image:: ../../_static/settings.png
	:height: 32px
	:align: middle

Environment and paths
~~~~~~~~~~~~~~~~~~~~~

The environment and path settings for the main TSI process and all 
its child processes (TSI workers) are controlled in the ``startup.properties``
file.

.. important::
  Please revise the path and environment settings in the main
  ``startup.properties`` config file.

These should include the path to all executables required by the TSI,
notably the batch system commands, and if applicable, the ACL
commands.

As the TSI process runs as root, and switches to the required
user/group IDs before each request, setting up the required
environment per user has to be done carefully. Per-user settings are
usually done on the UNICORE/X level using *IDB templates*, please
refer to the :ref:`UNICORE/X documentation <unicorex-manual>`.


Assigning groups to the current user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current user will all her groups assigned. On some systems the default
Python function used for resolving a user's groups does not see all
the groups. If this is the case, set in ``tsi.properties``::

  tsi.use_id_to_resolve_gids=true

This will use a different implementation via the system command
``id -G <username>``.


Batch system integration: BSS.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file `BSS.py <https://github.com/UNICORE-EU/tsi/blob/master/lib/BSS.py>`_
contains the functions specific to the used batch system,
specifically it prepares the job script, deals with job status 
reporting and job control.

Even if you run a well-supported batch system such as Torque or Slurm,
you should make sure that the job status reporting works properly.

Also, any site-specific resource settings (e.g. settings related to 
GPUs, network topology etc) are dealt within this file.

Reporting free disk space
~~~~~~~~~~~~~~~~~~~~~~~~~

UNICORE will often invoke the ``df`` command which is implemented in the
`IO.py 
<https://github.com/UNICORE-EU/tsi/blob/master/lib/IO.py>`_ file in order 
to get information about free disk space. On some
distributed file systems, executing this command can take quite some
time, and it may be advisable to modify the ``df`` function to
optimize this behaviour.

Reporting computing time budget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If supported by your site installation, users might have a computing time
budget allocated to them. The `BSS.py 
<https://github.com/UNICORE-EU/tsi/blob/master/lib/BSS.py>`_ module contains a 
function ``get_budget`` that is used to retrieve this budget as a number e.g. 
representing core-hours. By default, this function returns ``-1`` to indicate 
that computing time is not budgeted.

Filtering cluster working nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting from version 6.5.1 the TSI can filter nodes based on the properties
defined for nodes in BSS configuration. It can limit working nodes only to
those having shared file system. 
It can be defined in the ``tsi.properties`` file by setting the property ``tsi.nodes_filter``.

.. attention::
 Note that this feature is not working for all batch systems. Currently, it is 
 supported in Torque and SLURM.

Resource reservation
~~~~~~~~~~~~~~~~~~~~

The reservation module `Reservation.py 
<https://github.com/UNICORE-EU/tsi/blob/master/lib/Reservation.py>`_ is 
responsible for interacting with the reservation system of your batch system. 

.. attention::
 Note that this feature is not available for all batch systems. Currently, it is 
 included in Torque and SLURM.


|connections-img| Execution model
---------------------------------

.. |connections-img| image:: ../../_static/connections.png
	:height: 32px
	:align: middle

The main TSI process will respond to UNICORE/X requests and start
up TSI workers to do the work for the UNICORE/X server.
The TSI workers connect back to the UNICORE/X server.

It is possible to use the same TSI from multiple UNICORE/X servers.

Since the main TSI process runs with elevated privileges, it must
authenticate the source of commands as legitimate. To do this, the TSI
is initialised with the address(es) of the machine(s) that runs the
UNICORE/X. The TSI will only accept requests from the defined
UNICORE/X machine(s).  The callback port can be pre-defined in
``tsi.properties`` as well. If it is undefined, the TSI will attempt to
read it from the UNICORE/X connect message.

Note that it is possible to enable SSL on the TSI listen port, see below.
In SSL mode, there is no check of the UNICORE/X address.

If the UNICORE/X process shuts down, any TSI workers that are connected to
UNICORE/X will also shut down. However, the main TSI process will continue
executing and will spawn new TSI workers processes when the UNICORE/X server
is restarted. Therefore, it is not necessary to restart the TSI daemon
when restarting UNICORE/X.

If a TSI worker stops execution, UNICORE/X will request a new one to replace it.

If the main TSI process stops execution, then all TSI processes will also be killed.
The TSI must then be restarted, this does not happen automatically.


|authentication-img| PAM, systemd and user slices
-------------------------------------------------

.. |authentication-img| image:: ../../_static/authentication.png
	:height: 32px
	:align: middle


By default, user tasks (such as user scripts on the TSI node) will run in the same
slice as the TSI itself.

You can enable PAM, which will open a user session before running the user's tasks,
so the tasks will be run in the correct user slice, and thus the system's resource
management will properly apply also to tasks started via UNICORE.

To do this, set in ``tsi.properties``
::

  tsi.open_user_sessions=1

By default, a PAM module ``unicore-tsi`` is expected (``/etc/pam.d/unicore-tsi``).
For example, this could contain:

.. code::

  #%PAM-1.0
  auth	      sufficient    pam_rootok.so
  session     required	    pam_limits.so
  session     required	    pam_unix.so
  session     required      pam_systemd.so


|folders-img| Directories used by the TSI
-----------------------------------------

.. |folders-img| image:: ../../_static/folders.png
	:height: 32px
	:align: middle

The TSI must have access to the *filespace* directory specified in the
UNICORE/X configuration (usually the property ``XNJS.filespace`` in
``xnjs.properties``) to hold job directories. These directories are
written with the TSI's uid set to the Unix user for which the work is
being performed. If you use a shared directory for all users,
this directory must be world writable. The required Unix access mode is ``1777``.


|start-img| Running the TSI
---------------------------

.. |start-img| image:: ../../_static/start.png
	:height: 32px
	:align: middle

For the Linux packages, the TSI is pre-configured for systemd, and
if you want to run it as a a system service, you can use ``systemctl``:

.. code:: console

  $ sudo systemctl add-wants multi-user.target unicore-tsi-variant

(where *variant* stands for the concrete TSI implementation, such as
``nobatch`` or ``slurm``)


Starting 
~~~~~~~~

If installed from an Linux package, the TSI can be started via *systemd*:

.. code:: console

 $ sudo systemctl start unicore-tsi-variant


The TSI can also be started using the script ``BIN/start.sh``.

Stopping the TSI
~~~~~~~~~~~~~~~~

If installed from an Linux package, the TSI can be stopped via *systemd*:

.. code:: console

  $ sudo systemctl stop unicore-tsi-variant


The TSI can also be stopped using the script ``BIN/stop.sh``
(cf. section *Scripts*). This will stop the main TSI process and the tree
of all spawned processes including the TSI workers.

TSI worker processes (but not the main process) will stop executing when
the UNICORE/X server it connects to stops executing.

It is possible to stop a TSI worker process, but this could result in
the failure of a job (the UNICORE/X server will recover and create
new TSI processes).

TSI logging
~~~~~~~~~~~

By default, the TSI logs to the system journal (syslog), and you can read
the logs via ``journalctl``, for example,

.. code:: console

  $ sudo journalctl -u unicore-tsi-variant


To print logging output to stdout instead, set 
::

  tsi.use_syslog=false``

in the :file:`{CONF}/tsi.properties` file.


Since stdout is redirected to a file (see the STARTLOG definition in ``CONF/startup.properties``)
the logging output will be in that file.


For more verbose logging, set
::

  tsi.debug=true

in :file:`{CONF}/tsi.properties`.


|integration-img| Porting the TSI to other batch systems
--------------------------------------------------------

.. |integration-img| image:: ../../_static/integration.png
	:height: 32px
	:align: middle

Most variations are found in the batch subsystem commands, porting
to a new BSS usually requires changes to the following files:

* `BSS.py <https://github.com/UNICORE-EU/tsi/blob/master/lib/BSS.py>`_

* `Reservation.py <https://github.com/UNICORE-EU/tsi/blob/master/lib/Reservation.py>`_ 
  (reservation functions if applicable)

It is recommended to start from a up-to-date and well-documented TSI, e.g.
the Torque or Slurm variation. If you have further questions regarding porting
to a new batch system, please use the `unicore-support 
<mailto:unicore-support@lists.sf.net>`_ or `unicore-devel 
<mailto:unicore-devel@lists.sf.net>`_ mailing lists.

.. _tsi_security:

|security-img| Securing and hardening the system
------------------------------------------------

.. |security-img| image:: ../../_static/security.png
	:height: 32px
	:align: middle

In a normal multi-user production setting, the TSI runs with elevated
privileges, and thus it is critical to prevent illicit access to the
TSI, which would allow accessing or destroying arbitrary user data, as
well as impersonating users and generally wreaking havoc.

Once the connection to the UNICORE/X is established, the TSI is
controlled via a simple text-based API. An attacker allowed to connect
to the TSI can very easily execute commands as any valid (non-root)
user.

In non-SSL mode, the TSI checks the IP address of the connecting
process, and compare it with the expected one which is configured in the
``tsi.properties`` file.

In SSL mode, the TSI checks the certificate of the connecting process, by
validating it against its truststore which is configured in the ``tsi.properties`` 
file.

We recommed the following measures to make operating the TSI secure:

* Prevent all access to the TSI's config and executable files. This is usually
  done by setting appropriate file permissions, and usually already taken care 
  of during installation ( please see the section :ref:`tsi_permissions`).

* Make sure only UNICORE/X can connect to the TSI. This is most reliably done by 
  configuring SSL for the UNICORE/X to TSI communication (please see the section 
  :ref:`tsi_ssl`).

* If SSL cannot be used, the UNICORE/X should run on a separate machine.

* On the UNICORE/X machine, user login should be impossible. This will
  prevent bypassing the IP check (in non-SSL mode) and/or accessing
  the UNICORE/X private key (in SSL mode).

* If you for some reason HAVE to run UNICORE/X and TSI on the same
  machine, and user login or execution of user commands is possible
  on that machine, you **MUST use SSL**, and take special care to protect
  the UNICORE/X config files and keystore using appropriate file
  permissions. Not using SSL in this situation is a serious risk! An
  attacker connecting to the TSI can impersonate any user and access 
  any user's data (except for the *root* user).

* An additional safeguard is to establish monitoring for UNICORE/X, and 
  kill the TSI in case the UNICORE/X process terminates.

.. important::
  Summarizing, it is critical to protect config files and executable
  files. We strongly recommend to configure SSL. Using SSL is a **MUST**
  in deployments where users can login to the UNICORE/X machine.


.. raw:: html

   <hr>
