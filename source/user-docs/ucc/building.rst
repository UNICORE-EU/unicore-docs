.. _ucc-building:

Building UCC packages
=====================

Prerequisites
-------------

You need Java and Apache Maven. 
Check the versions given in the `pom.xml 
<https://github.com/UNICORE-EU/commandline-client/blob/master/pom.xml>`_ file.

Building Java code 
------------------

If not already done, build the jars from the *root* dir:

.. code:: console

 $ cd .. ; mvn clean install -DskipTests


Creating distribution packages
------------------------------

The following commands create the distribution packages
in ``tgz``, ``deb`` and ``rpm`` formats (**Maven 2!**). The versions
are taken from the `pom.xml 
<https://github.com/UNICORE-EU/commandline-client/blob/master/pom.xml>`_.

tgz
~~~

.. code:: console

 $ mvn package -DskipTests -Ppackman -Dpackage.type=bin.tar.gz
 
deb
~~~

.. code:: console

 $ mvn package -DskipTests -Ppackman -Dpackage.type=deb -Ddistribution=Debian


rpm redhat
~~~~~~~~~~

.. code:: console

 $ mvn package -DskipTests -Ppackman -Dpackage.type=rpm -Ddistribution=RedHat