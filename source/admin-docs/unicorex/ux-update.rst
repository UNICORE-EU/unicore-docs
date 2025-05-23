.. _unicorex-update:

|update-img| UNICORE/X Update
-----------------------------

.. |update-img| image:: ../../_static/update.png
	:height: 32px
	:align: middle

As a first step and precaution, you should make backups of your 
existing config files and put them in a safe place.

In the following, *LIB* refers to the directory containing the jar files for the component, and *CONF* to the config directory of the existing installation.

* It is assumed that you have unpacked the **tar.gz** file somewhere, e.g. to ``/tmp/``. In the following, this location will be denoted as "`$NEW`":

  .. code:: console

	$ export NEW=/tmp/unicore-servers-9.0.0

* Stop the server. If not yet done, make a backup of the config files.

* Update the jar files:

  .. code:: console

   	$ rm -rf LIB/*
   	$ cp $NEW/lib/*.jar LIB

* Start the server.

* Check the logs for any **ERROR** or **WARN** messages and if necessary correct them.


.. raw:: html

   <hr>
