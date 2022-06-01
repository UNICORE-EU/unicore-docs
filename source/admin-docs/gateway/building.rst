.. _gateway-building:

Building distribution packages
==============================

Prerequisites
-------------

You need Java 11 and Apache Maven.


Buiding Java code
-----------------

The Java code is built and unit tested using

.. code:: console

  $ mvn install

To skip unit testing

.. code:: console

  $ mvn install -DskipTests


Creating distribution packages
------------------------------

The following commands create the distribution packages
in tgz, deb and rpm formats

The package versions are defined in the `pom.xml 
<https://github.com/UNICORE-EU/gateway/blob/master/pom.xml>`_ file!

tgz
~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=bin.tar.gz

deb
~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=deb -Ddistribution=Debian

rpm
~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=rpm -Ddistribution=RedHat



