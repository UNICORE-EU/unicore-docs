.. _gateway-building:

Building distribution packages
==============================

Prerequisites
-------------

You need Java 7 and Apache Maven.

.. note::
  For packaging, you'll need maven2, while for other 
  tasks both 2 and 3 should work.


Buiding Java code
-----------------

The Java code is built and unit tested using

.. code:: console

  $ mvn install

To skip unit testing

.. code:: console

  $ mvn install -DskipTests


Creating documentation
----------------------

To build the docs:

.. code:: console

  $ mvn site

You can check them by pointing a web browser at 
``target/site/index.html``

To upload the docs to the unicore-dev documentation server:

.. code:: console

  $ mvn site:deploy


Creating distribution packages
------------------------------

The following commands create the distribution packages
in tgz, deb and rpm formats

The package versions are defined in the ``pom.xml`` file!

tgz
~~~

.. code:: console

  $> mvn package -DskipTests -Ppackman -Dpackage.type=bin.tar.gz

deb
~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=deb -Ddistribution=Debian

rpm
~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=rpm -Ddistribution=RedHat



