.. _xuudb-building:

Building the XUUDB 
==================

Prerequisites
-------------

Apart from the Java SDK, you will need a Git client and Maven3, 
available at https://maven.apache.org.

Buiding
-------

#) Checkout the `code <https://github.com/UNICORE-EU/xuudb>`_ from 
   the Github
   
   .. code:: console
  
      $ git clone https://github.com/UNICORE-EU/xuudb.git

#) To compile the components, do
  
   .. code:: console
  
     $ mvn clean install

#) Packaging

   After compiling, change into the ``xuudb-all`` directory:

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


#) To setup eclipse for developing XUUDB code,

   .. code:: console
  
      $ mvn eclipse:eclipse

   which will generate Eclipse project files and in Eclipse use 
   :menuselection:`Import --> Existing projects into Workspace...` to import the 
   projects into Eclipse.




