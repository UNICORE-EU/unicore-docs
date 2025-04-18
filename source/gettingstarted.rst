.. _unicore-gettingstarted:

|start-img| Getting started
***************************

.. |start-img| image:: _static/start.png
	:height: 32px
	:align: middle


Using UNICORE
-------------

If you are an end-user or application developer who wishes to use
an existing UNICORE installation, have a look at the user documentation
for the :ref:`UNICORE Commandline Client <ucc>`, the 
`PyUNICORE <https://pyunicore.readthedocs.io/>`_ client library
or the :ref:`REST API documentation <rest-api>`.

Evaluating UNICORE
------------------

If you wish to experiment with a UNICORE server installation, one simple way is to
download the `Core Server Bundle <https://github.com/UNICORE-EU/server-bundle/releases>`_
which can be installed very quickly on a single test machine or even your laptop.

If you are a `Docker <https://docs.docker.com>`_ user, you can try our
`UNICORE Docker image <https://github.com/UNICORE-EU/tools/tree/master/unicore-docker-image>`_.

Deploying UNICORE
-----------------

Full production deployments of UNICORE range from minimalistic to rather complex, depending
on your requirements, use cases and existing infrastructure. 

For the typical case of providing UNICORE access to a single compute cluster, please have a look
at :ref:`How to setup UNICORE for a single HPC cluster <unicore-howto-singlecluster>`.

For more complex cases, here are a few starting points:

1. for each target resource (e.g. a compute cluster) you need a :ref:`TSI <tsi>` and 
   a :ref:`UNICORE/X<unicorex>`.
   The TSI is deployed on the cluster login node(s), while UNICORE/X requires a VM or server,
   UNICORE/X should NOT be run on a machine where users can log in.

2. we strongly recommend running a :ref:`Gateway <gateway>`, one for all of an
   institution/company's UNICORE services is enough. This will shield the services from direct
   external access for added security.
  
3. For the services (except TSI where this is optional), you will need server certificate(s)
   from a CA (similar to a web server)

4. for multi-site workflows, you will need a :ref:`Registry <registry>` 
   and a :ref:`Workflow service <workflow>`

.. raw:: html

   <hr>
