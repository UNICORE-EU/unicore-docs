.. _gateway-manual:


|user-guide| Gateway Manual
===========================

.. |user-guide| image:: ../../_static/user-guide.png
	:height: 32px
	:align: middle

The Gateway is the entry point into a UNICORE site, routing HTTPS
traffic to servers like :ref:`unicorex`. It forwards client traffic to the
intended destination, optionally authenticating the client. The
Gateway receives the reply and sends it back to the client. In this
way, only a single open port in a site's firewall has to be
configured.

.. attention:: **LIMITATIONS**
  
  The Gateway is not a complete HTTP reverse proxy implementation. For
  example, it is not possible to run a full, complex web      application
  *behind* the Gateway, especially not if protocols like    WebSocket are
  used.

In effect, traffic to a *virtual* URL, e.g.
*\https://mygateway:8088/Alpha* is forwarded to the real URL, e.g.
*\https://host1:7777*.

The mappings of virtual URL to real URL for the available sites are
listed in a configuration file ``connections.properties``.
Additionally, the Gateway supports dynamic registration of sites.

The second functionality of the Gateway is (optional) authentication 
of incoming requests. Connections to the Gateway are made using SSL, 
so the Gateway can be configured to check whether the caller presents 
a certificate issued by a trusted authority. Information about the 
client is forwarded to services behind the Gateway in UNICORE proprietary 
format (as a SOAP or HTTP header).

The Gateway will forward the IP address of the client to the back-end server.

Last not least, the Gateway can be configured as a HTTP load balancer.

.. important:: IMPORTANT NOTE ON PATHS

  Depending on the installation method, the paths to various Gateway files 
  are different. If installing using a distribution-specific package the 
  following paths are used::

    CONF=/etc/unicore/gateway
    BIN=/usr/sbin
    LOG=/var/log/unicore/gateway

  If installing using the portable bundle all Gateway files are installed
  under a single directory. Path prefixes then are as follows, where *INST* 
  is a directory where the Gateway was installed::

    CONF=INST/conf
    BIN=INST/bin
    LOG=INST/logs

  The above variables (*CONF*, *BIN* and *LOG*) are used throughout the rest of 
  this manual.


|install-img| Installation 
--------------------------

.. |install-img| image:: ../../_static/installer.png
	:height: 32px
	:align: middle

The UNICORE Gateway is distributed in the following formats:

#. As a part of platform independent installation bundle called
   `UNICORE Server bundle <https://github.com/UNICORE-EU/server-bundle/releases>`_.  
   The UNICORE Server bundle is provided as a tar package and includes a command line installer.
#. As a binary, platform-specific package available for
   RedHat (Centos) and Debian platforms (currently not publicly available)


Prerequisites
~~~~~~~~~~~~~

To run, the Gateway requires Java (JRE headless is sufficient) in
version 11 or later. We recommend using 
`OpenJDK <https://openjdk.java.net/install/>`_.


Installation from the Server bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download `the server bundle <https://github.com/UNICORE-EU/server-bundle/releases>`_
from the UNICORE project website. 

Please review the ``README`` file available after extracting the
bundle. You don't have to change any defaults as the Gateway is
installed by default.

You should create and use a system user (e.g. *unicore*) to   install
and run the gateway. For security reasons, **do not** run the   Gateway as
the *root* user.


Installation from a Linux package (rpm or deb)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use your distribution's package manager to install.


|update-img| Upgrading
----------------------

.. |update-img| image:: ../../_static/update.png
	:height: 32px
	:align: middle

The general update procedure is presented below, with possible variations:

#. Stop the old Gateway.

#. Update the server package. This step mostly applies for RPM/DEB managed installations. 
   For Quickstart installation it is enough to replace the ``*.jar`` files with the new ones.

#. Start the newly installed Gateway.

#. Verify log file and fix any problems reported.


|config-img| Configuration
--------------------------

.. |config-img| image:: ../../_static/configuration.png
	:height: 32px
	:align: middle

The Gateway is configured using a set of configuration files, which
reside in the ``CONF`` subdirectory.


Java and environment settings: ``startup.properties``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file contains settings related to the Java VM, such as the Java command
to use, memory settings, library paths, etc.

Configuring sites: ``connections.properties``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a simple list connecting the names of sites and their physical addresses. 
An example is::

  DEMO-SITE = https://localhost:7777
  REGISTRY = https://localhost:7778


If this file is modified, the Gateway will re-read it at runtime, so there is no need to 
restart the Gateway in order to add or remove sites.

Optionally, an administrator can enable a possibility for dynamic site registration at runtime, 
see :ref:`dyn-reg` for details. Then this file should contain only the 
static entries (or none if all sites register dynamically).

Further options for back-end sites configuration are presented in 
:ref:`loadbalance`.


Main server settings: ``gateway.properties``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``gateway.hostname`` property to configure the network interface and 
port the Gateway will listen on. You can also select between ``https`` and ``http`` protocol,  
though in almost all cases https will be used.

Example:: 

  gateway.hostname = https://192.168.100.123:8080

.. note:: 
  If you set the host to ``0.0.0.0``, the Gateway will listen on all network interfaces 
  of the host machine, else it will listen only on the specified one.

If the scheme of the hostname URL is set to ``https``, the Gateway uses the configuration 
data from ``security.properties`` to configure the HTTPS settings. 


Credential and truststore settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Gateway credential and truststore is configured using the following properties

.. csv-table:: Credential settings
  :file: tables/sec-ref-credProperties.csv
  :widths: 25, 15, 15, 45
  :header-rows: 1
  :class: tight-table
    

.. csv-table:: Truststore settings
  :file: tables/sec-ref-trustProperties.csv
  :widths: 25, 15, 15, 45
  :header-rows: 1
  :class: tight-table


Scalability settings
^^^^^^^^^^^^^^^^^^^^

To fine-tune the operational parameters of the embedded Jetty server, you can set 
advanced HTTP server parameters (see :ref:`ref-jetty` for details). 
Among others you can use the non-blocking IO connector offered by Jetty, 
which will scale up to higher numbers of concurrent connections than the default connector. 

The Gateway acts as a https client for the VSites behind it. 
The number of concurrent calls is limited, and controlled by two parameters::

  # maximum total number of concurrent calls to Vsites
  gateway.client.maxTotal=100
  # total number of concurrent calls per site
  gateway.client.maxPerService=20


You can also control the limit on the maximum SOAP header size which
is allowed by the Gateway. Typically you **don't have to touch this
parameter**. However, if your clients do produce very big SOAP headers
and the Gateway blocks them, you can increase the limit. Note that
such a giant SOAP header usually means that the client is not behaving
as intended, e.g. is trying to perform a DoS attack.
::

 # maximum size of an accepted SOAP header, in bytes
 gateway.soapMaxHeader=102400

.. note::
 The Gateway may consume this amount of memory (plus some extra amount
 for other data) for each opened connection. Therefore, this value multiplied by 
 the number of maximum allowed connections, should be **significantly lower**, then the total
 memory available for the Gateway.
  

.. _dyn-reg:

Dynamic registration of Vsites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dynamic registration is controlled by three properties in ``CONF/gateway.properties`` file::

  gateway.registration.enable=true
  gateway.registration.secret=<your secret>

If set to ``true``, the Gateway will accept dynamic registrations which are made by 
sending a ``HTTP POST`` request to the URL ``/VSITE_REGISTRATION_REQUEST``.
This request must contain a parameter ``secret`` which matches the
value configured in the ``gateway.properties`` file.

Filters can be set to forbid access of certain hosts, or to require certain strings 
in the Vsite addresses. For example,
::

  gateway.registration.deny=foo.org example.org

will deny registration if the remote hostname contains *foo.org* or *example.org*. 
Conversely,
::

 gateway.registration.allow=mydomain.org

will only accept registrations if the remote address contains *mydomain.org*.
These two (deny and allow) can be combined.


Web interface (*monkey page*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For testing and simple monitoring purposes, the Gateway displays a
website showing detailed site information (the details view can be
disabled).  Once the Gateway is running, open up a browser and
navigate to :file:`https://{<gateway_host>}:8080` (or whichever URL the gateway
is running on).  If the Gateway is configured to do SSL
authentication, you will need to import a suitable client certificate
into your web browser.

A HTML form for testing the dynamic registration is available as well, 
by clicking the link in the footer of the main Gateway page.

To disable the Vsite details page, set 
::

  gateway.disableWebpage=true



Main options reference
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
  :file: tables/gw-ref-main.csv
  :widths: 30, 15, 15, 50
  :header-rows: 1
  :class: tight-table

.. _ref-jetty:

HTTP server settings
++++++++++++++++++++

.. _Java_cipher_names: https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html#SupportedCipherSuites

.. csv-table::
  :file: tables/sec-ref-jettyProperties.csv
  :widths: 30, 15, 15, 50
  :header-rows: 1
  :class: tight-table


Require end-user certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using client certificates for end-user authentication are **not required**
or recommended.  If you still want to require end-users to have a
certificate, the Gateway can be configured accordingly.
Set the following in ``gateway.properties``::

  gateway.httpServer.requireClientAuthn=true


Logging
^^^^^^^

UNICORE uses Log4j (version 2) as its logging framework, and
comes with an example configuration file (:file:`{CONF}/logging.properties`).

Please refer to the `Log4j documentation <https://logging.apache.org/log4j/2.x/manual/configuration.html>`_
for more information.


The most important, root log categories used by the Gateway's logging are:

.. table::
 :width: 100
 :widths: 40 60
 :class: tight-table
 
 +----------------------+-------------------------+
 | **unicore.gateway**  | General Gateway logging |
 +----------------------+-------------------------+
 | **unicore.security** | Certificate details and |
 |                      | other security          |           
 +----------------------+-------------------------+
 | **org.apache.http**  | Outgoing HTTP to the    |
 |                      | backend services        |
 +----------------------+-------------------------+             


.. _apache:

|apache-img| Using Apache httpd as a frontend
---------------------------------------------

.. |apache-img| image:: ../../_static/apache.png
	:height: 32px
	:align: middle

You may wish to use the Apache webserver (httpd) as a 
frontent for the Gateway (e.g. for security or fault-tolerance reasons).

Requirements
~~~~~~~~~~~~

 - `Apache httpd <https://httpd.apache.org/>`_
 - `mod_proxy <https://httpd.apache.org/docs/2.4/mod/mod_proxy.html>`_ for Apache httpd

External references
~~~~~~~~~~~~~~~~~~~

  - https://wiki.eclipse.org/Jetty/Howto/Configure_mod_proxy


.. _loadbalance:

|load-balance-img| Using the Gateway for failover and/or loadbalancing of UNICORE sites
---------------------------------------------------------------------------------------

.. |load-balance-img| image:: ../../_static/load-balancer.png
	:height: 32px
	:align: middle


The Gateway can be used as a simple failover solution and/or loadbalancer to achieve 
high availability and/or higher scalability of UNICORE/X sites without additional tools.

A site definition (in :file:`{CONF}/connections.properties`) can be extended, so that multiple physical 
servers are used for a single virtual site. 

An example for such a so-called multi-site declaration in the ``connections.properties`` file 
looks as follows::

 #declare a multisite with two physical servers
 
 MYSITE=multisite:vsites=https://localhost:7788 https://localhost:7789

This will tell the Gateway that the virtual site *MYSITE* is indeed a multi-site with the
two given physical sites.

Configuration
~~~~~~~~~~~~~

Configuration options for the multi-site can be passed in two ways. On the one hand they can
go into the ``connections.properties`` file, by putting them in the multi-site definition, separated
by ``;`` characters::

  #declare a multisite with parameters

  MYSITE=multisite:param1=value1;param2=value2;param3=value3;...


The following general parameters exist:

.. table::
 :width: 100
 :widths: 30 70
 :class: tight-table
 
 +--------------+----------------------------------+
 | **vsites**   | List of physical sites           |
 +--------------+----------------------------------+
 | **strategy** | Class name of the site selection |
 |              | strategy to use (see below)      |
 +--------------+----------------------------------+
 | **config**   | Name of a file containing        |
 |              | additional parameters            |
 +--------------+----------------------------------+

Using the ``config`` option, all the parameters can be placed in a separate file for enhanced 
readability. For example, you could define in ``connections.properties``::

  #declare a multisite with parameters read from a separate file
  
  MYSITE=multisite:config=conf/mysite-cluster.properties


and give the details in the file ``conf/mysite-cluster.properties``::

  #example multisite configuration
  vsites=https://localhost:7788 https://localhost:7789
  
  #check site health at most every 5 seconds 
  strategy.healthcheck.interval=5000


Available strategies
~~~~~~~~~~~~~~~~~~~~

A selection strategy is used to decide where a client request will
be routed. By default, the strategy is "**Primary with fallback**", i.e. the request 
will go to the first site if it is available, otherwise it will go to the second site.

Primary with fallback
^^^^^^^^^^^^^^^^^^^^^

This strategy is suitable for a high-availability scenario,   where a secondary site takes over
the work in case the primary one goes down for maintenance or   due to a problem. This is the
default strategy, so nothing needs to be configured to enable   it. If you want to explicitely
enable it anyway, set
::

  strategy=primaryWithFallback

The strategy will select from the first two defined physical sites. The first, primary one will
be used if it is available, else the second one. Health check is done on each request, but not
more frequently as specified by the ``strategy.healthcheck.interval`` parameter. By default, this parameter
is set to ``5000`` milliseconds.

Changes to the site health will be logged at ``INFO`` level, so you can see when the sites go up or down.

Round robin
^^^^^^^^^^^

This strategy is suitable for a load-balancing scenario, where  a random site will be chosen from
the available ones. To enable it, set
::

   strategy=roundRobin

Changes to the site health will be logged at ``INFO`` level, so  you can see when the sites go up or down.

**It is very important** to be aware that this strategy requires   that all backend sites used in the pool,
share a common persistence. It is because Gateway does not track clients, so particular client requests
may land at different sites. This is typically solved by using a non-default, shared database for sites,
such as MySQL.

.. caution::
  Currently loadbalancing of target sites is an experimental feature and is not yet fully functional.
  It will be improved in future UNICORE versions.


Custom strategy
^^^^^^^^^^^^^^^

You can implement and use your own failover strategy, in this case, use the name of the Java class as
strategy name::

  strategy=your_class_name


|failover-img| Gateway failover and migration
---------------------------------------------

.. |failover-img| image:: ../../_static/failover.png
	:height: 32px
	:align: middle

The :ref:`loadbalance` covered usage of the Gateway to provide failover of backend services.
However, it may be needed to guarantee high-availabilty for the Gateway itself or to move it
to other machine in case of the original one's failure.

Gateway's migration
~~~~~~~~~~~~~~~~~~~

The Gateway does not store any state information, therefore its migration is easy. 
It is enough to install the Gateway at the target machine (or even to simply copy 
it in the case of installation from the core server bundle) and to make sure that 
the original Gateway's configuration is preserved. 

If the new machine uses a different address, it needs to be reflected in the 
server's configuration file (the listen address). Also, the
configuration of sites behind the Gateway must be updated accordingly. 


Failover and loadbalancing of the Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gateway itself doesn't provide any features related to its own redundancy. However, as it 
is stateless, the standard redundancy solutions can be used.

The simpliest solution is to use Round Robin DNS, where DNS server routes the Gateway's DNS
address to a pool of real IP addresses. While easy to set up this solution has a
significant drawback: DNS server doesn't care about machines being down.


.. raw:: html

   <hr>
