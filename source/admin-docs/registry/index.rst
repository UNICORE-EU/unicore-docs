.. _registry:

Registry 
********

The Registry server provides information about available services to clients and other 
services. It is a specially configured :ref:`UNICORE/X <unicorex>` server, so please make sure 
to read the general :ref:`UNICORE/X manual <unicorex-manual>` as well.

Multiple UNICORE/X sites can share a Registry, greatly simplifying the use of UNICORE services. 
Since such a registry is vital to the functioning of a UNICORE-based federation, you can have 
more than one.


|install-img| Installation
--------------------------

.. |install-img| image:: ../../_static/installer.png
	:height: 32px
	:align: middle

Prerequisites
~~~~~~~~~~~~~ 

To run the Registry, you need a Java runtime (headless is enough), in version 11 or later.

UNICORE servers have been most extensively tested on Linux systems, but run on MacOS/X as well.

Please note that

- to integrate into secure production environments, you will need access to a certificate 
  authority and generate server certificates for all your UNICORE servers.

- to make your UNICORE servers accessible outside of your firewalls,
  you should setup and configure a :ref:`UNICORE Gateway <gateway>`.


A note on paths
~~~~~~~~~~~~~~~

The Registry can be installed either from the `UNICORE Server bundle  
<https://sourceforge.net/projects/unicore/files/Servers/Core/>`_ (tar.gz or zip archive) or 
from a Linux package on the `UNICORE project website 
<https://sourceforge.net/p/unicore/wiki/Linux_Repositories/>`_ at sourceforge  
(i.e. RPM or deb). 

.. attention::

  Using the Linux packages, you can install only a single Registry instance per machine 
  (without manual changes).

The following table gives an overview of the file locations for both
tar.gz and Linux packages:

.. table::
 :width: 100
 :widths: 15 20 40 25
 :class: tight-table
 
 +---------+--------------------+-----------------------------------+----------------+
 | Name in | tar.gz,  zip       | rpm                               | Description    |
 | this    |                    |                                   |                |
 | manual  |                    |                                   |                |
 +=========+====================+===================================+================+
 | CONF    | <basedir>/conf/    | /etc/unicore/registry             | Config files   |
 +---------+--------------------+-----------------------------------+----------------+
 | LIB     | <basedir>/lib/     | /usr/share/unicore/registry/lib   | Java libraries |
 +---------+--------------------+-----------------------------------+----------------+
 | LOG     | <basedir>/log/     | /var/log/unicore/registry/        | Log files      |
 +---------+--------------------+-----------------------------------+----------------+
 | BIN     | <basedir>/bin/     | /usr/sbin/                        | Start/stop     |
 |         |                    |                                   | scripts        |
 +---------+--------------------+-----------------------------------+----------------+


|config-img| Registry configuration
-----------------------------------

.. |config-img| image:: ../../_static/configuration.png
	:height: 32px
	:align: middle


A Registry is running in a *normal* :ref:`UNICORE/X <unicorex>` container, however, you
should use a dedicated UNICORE/X instance for the Registry, making sure no other services 
are running.

Thus, most of the UNICORE/X documentation regarding access control, keystores, etc also applies 
to the Registry. Please, make sure to read the :ref:`UNICORE/X documentation <unicorex-manual>` 
as well.


Registry configuration (``CONF/uas.config``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apart from hostname, port, and other properties, the ``uas.config`` file must contain the 
following entry::

 container.feature.Registry.mode=shared

This setting configures the container to operate as a shared Registry.


Starting and stopping
~~~~~~~~~~~~~~~~~~~~~

The Registry is started and stopped like any other 
:ref:`UNICORE/X <unicorex>` container using the scripts in the ``bin`` folder.

.. _access-control:

Access control
~~~~~~~~~~~~~~

It is absolutely **VITAL** that the Registry only contains **trusted
entries**. Therefore the default access control policies (``CONF/xacml2Policies/*.xml``)
only allow to add entries only for callers with the role *server*.

You will need to map the certificates / DNs of all servers wishing to publish into the registry
as having the role *server*.  Please check the :ref:`UNICORE/X documentation <unicorex-manual>`
on how to do that, using an XUUDB or other attribute source.


User / server authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While users can read registry content without needing to be authenticated,
servers **MUST** be authenticated and mapped to role *server* to be able
to write to the Registry.

To accept servers, the REST interface must be configured for X509
authentication.

As an example the following configuration will achieve this::

  #
  # Authentication for the REST interface
  #
  container.security.rest.authentication.order=X509
  container.security.rest.authentication.X509.class=eu.unicore.services.rest.security.X509Authenticator


For further details we refer also to the :ref:`UNICORE/X documentation <unicorex-manual>` on
authentication and REST services.


Gateway configuration
~~~~~~~~~~~~~~~~~~~~~

If running the Registry behind a :ref:`gateway`, you'll need to add an entry
to the Gateway's site list file (``connections.properties``) that points
to your Registry server. Another option is to use dynamic
registration. In the following, we assume the Registry is named
*REGISTRY*.


UNICORE/X configuration
~~~~~~~~~~~~~~~~~~~~~~~

To publish the services in a shared registry, configure the
address of the registry in ``uas.config``::

  # switch on use of external registry 
  container.externalregistry.use=true
  
  # URL
  container.externalregistry.url=https://...
  
  # optionally you can have more registries
  container.externalregistry.url.2=https://...

The entries in the global Registry are updated at a specified
interval. To control this interval, edit a property in
``CONF/container.properties``::

  # default termination time for registry entries in seconds
  container.wsrf.sg.defaulttermtime=1800

  
Client configuration
~~~~~~~~~~~~~~~~~~~~

Clients will require the URL of a Registry.
For example, in the :ref:`UCC <ucc>` preferences file (supply the correct 
values for your setup)::

  registry=https://gwhost:port/REGISTRY/rest/registries/default_registry

.. raw:: html

   <hr>
