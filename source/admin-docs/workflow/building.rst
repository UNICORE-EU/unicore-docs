.. _workflow-building:

Building the Workflow Service 
=============================

Prerequisites
-------------

You need Java, Apache Ant and Apache Maven 3.


Building
--------

The following commands create the distribution packages.

deb
~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=deb -Ddistribution=Debian


rpm
~~~
  
.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=rpm -Ddistribution=RedHat


binary tar.gz
~~~~~~~~~~~~~

.. code:: console

  $ mvn package -DskipTests -Ppackman -Dpackage.type=bin.tar.gz



