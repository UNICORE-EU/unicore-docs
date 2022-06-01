.. _unicorex-building:

Building UNICORE/X and Registry
===============================

Prerequisites
-------------

You need Java 11 or later and Apache Maven.


Building Java code 
------------------

The Java code is built and unit tested using

.. code:: console

  $ mvn install

To skip unit testing and save lots of time:

.. code:: console

  $ mvn install -DskipTests


Creating distribution packages
------------------------------

The following commands create the distribution packages
in tgz, deb and rpm formats

Do a ``cd unicorex-dist`` or ``cd registry-dist`` for UNICORE/X or
Registry.

The versions are defined in the `pom.xml 
<https://github.com/UNICORE-EU/unicorex/blob/master/unicorex-dist/pom.xml>`__ file!

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



