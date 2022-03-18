.. _unicorex-building:

Building UNICORE/X and Registry
===============================

Prerequisites
-------------

You need Java 8 or later and Apache Maven.


Building Java code 
------------------

The Java code is built and unit tested using

.. code:: console

  $ mvn install

To skip unit testing and save lots of time:

.. code:: console

  $ mvn install -DskipTests


Creating documentation
----------------------

For UNICORE/X, do

.. code:: console

  $ cd unicorex-dist

and check that the versions in `pom.xml 
<https://github.com/UNICORE-EU/unicorex/blob/master/pom.xml>`_ are OK. The manual sources
are asciidoc txt files in src/doc, some parts are included from
the general `USE <https://github.com/UNICORE-EU/use>`__ documentation.

To build the docs:

.. code:: console

  $ mvn site

You can check them by pointing a web browser at 
``target/site/index.html``

To upload the docs to the unicore-dev documentation server:

.. code:: console

  $ mvn site:deploy

For the registry it is the same, only in the ``registry-dist`` folder.


Creating distribution packages
------------------------------

The following commands create the distribution packages
in tgz, deb and rpm formats

Do a ``cd unicorex-dist`` or ``cd registry-dist`` for UNICORE/X or
Registry.

The versions are again defined in the `pom.xml 
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



