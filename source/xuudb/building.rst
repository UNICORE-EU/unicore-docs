.. _xuudb-building:

Building the XUUDB 
==================

Prerequisites
-------------

Apart from the Java SDK, you will need a Git client and Maven3, 
available at http://maven.apache.org

Buiding
-------

1) Checkout the code from the Github
   
   .. code:: console
  
      $ git clone https://github.com/UNICORE-EU/xuudb.git

2) To compile the components, do
  
   .. code:: console
  
     $ mvn clean install

3) Packaging

   After compiling, change into the xuudb-all directory:

   .. code:: console
  
     $ cd xuudb-all
   
   To build packages in different formats:
   
   * **tar.gz**
   
   
     .. code:: console
     
       $ mvn package -DskipTests -Ppackman -Dpackage.type=bin.tar.gz

   * **deb**
   
     .. code:: console
  
       $ mvn package -DskipTests -Ppackman -Dpackage.type=deb -Ddistribution=Debian

   * **rpm**
  
     .. code:: console
  
       $ mvn package -DskipTests -Ppackman -Dpackage.type=rpm -Ddistribution=RedHat


4) To setup eclipse for developing XUUDB code,

.. code:: console
  
   $ mvn eclipse:eclipse

which will generate Eclipse project files
and in Eclipse use "Import/Existing projects into Workspace..."
to import the projects into Eclipse


CONTACT INFO
~~~~~~~~~~~~

Web:            https://www.unicore.eu
Mailing lists:  https://sourceforge.net/projects/unicore
Sources:        https://github.com/UNICORE-EU/xuudb



