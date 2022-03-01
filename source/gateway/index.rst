.. _gateway:

Gateway
*******

The UNICORE Gateway is an (optional) server component that
provides a reverse https proxy, allowing you to run several backend
servers (:ref:`unicorex`, Registery, ...) behind a single address.
This helps with firewall configuration, requiring only a **single open port** (a similar effect can be achieved using other http servers that can
act as a reverse proxy, such as **Apache httpd** or **nginx**).


The second functionality of the Gateway is (optional) authentication
of incoming requests. Connections to the Gateway are made using SSL,
so the Gateway can be configured to check whether the caller presents
a certificate issued by a trusted authority. Information about the
client is forwarded to services behind the Gateway in UNICORE
proprietary format (as a SOAP or HTTP header).

The Gateway will forward the IP address of the client to the back-end
server.

Last not least, the Gateway can be configured as a HTTP load balancer.




.. image:: ../_static/unicore-arch.png
  :width: 600
  :alt: UNICORE architecture


:doc:`manual`
  Installation and Operating the Gateway.

:doc:`building`
  Buiding the distribution packages.



:doc:`changelog`
    The Gateway changelog.
    

.. toctree::
	:maxdepth: 1
	:caption: Gateway Documentation
	:hidden:
	
	manual
	building

.. toctree::
	:maxdepth: 1
	:hidden:
	
	changelog


