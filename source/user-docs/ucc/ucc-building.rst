.. _ucc-building:

|app-package-img| Building the UCC
==================================

.. |app-package-img| image:: ../../_static/app-package.png
	:height: 32px
	:align: middle

Prerequisites
-------------

You need Java and Apache Maven. 
Check the versions given in the `pom.xml 
<https://github.com/UNICORE-EU/commandline-client/blob/master/pom.xml>`_ file.

Building Java code 
------------------

Clone the git repo and build the jars from the *root* dir:

.. code:: console

 $ git clone https://github.com/UNICORE-EU/commandline-client.git
 $ cd commandline-client
 $ mvn clean install -DskipTests


Creating distribution packages
------------------------------

The following commands create the distribution packages
in *tgz*, *deb* and *rpm* formats. The versions
are taken from the `pom.xml 
<https://github.com/UNICORE-EU/commandline-client/blob/master/pom.xml>`_.

tgz
~~~

.. code:: console

 $ cd distribution
 $ mvn package -DskipTests -Ppackman -Dpackage.type=bin.tar.gz
 
deb
~~~

.. code:: console

 $ cd distribution
 $ mvn package -DskipTests -Ppackman -Dpackage.type=deb -Ddistribution=Debian


rpm redhat
~~~~~~~~~~

.. code:: console

 $ cd distribution
 $ mvn package -DskipTests -Ppackman -Dpackage.type=rpm -Ddistribution=RedHat
 
 
.. raw:: html

  <hr>
