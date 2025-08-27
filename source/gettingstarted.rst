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
See also :ref:`unicore-howto-testmachine` for more information.

If you are a `Docker <https://docs.docker.com>`_ user, you can try our
`UNICORE Docker image <https://github.com/UNICORE-EU/tools/tree/master/unicore-docker-image>`_.

Deploying UNICORE
-----------------

Full production deployments of UNICORE range from minimalistic to rather complex, depending
on your requirements, use cases and existing infrastructure. 

For the typical case of providing UNICORE access to a single compute cluster, please have a look
at :ref:`How to setup UNICORE for a single HPC cluster <unicore-howto-singlecluster>`.

For more complex cases, here are a few starting points:

1. For each target resource (e.g., a compute cluster), you need a
   :ref:`TSI <tsi>` and a :ref:`UNICORE/X <unicorex>`.

   The TSI is deployed on the cluster's login node(s). UNICORE/X, in
   contrast, should run on a separate server or virtual machine.

   UNICORE/X should **not** be run on a system where users can log in.

2. We strongly recommend running a :ref:`Gateway <gateway>`.
   
   One gateway is sufficient for all UNICORE services at an institution
   or company.

   This component shields backend services from direct external access,
   providing an important layer of security.
  
3. For the services (except TSI, where this is optional), you will need
   server certificate(s) issued by a trusted Certificate Authority (CA),
   similar to what is used for web servers.

4. For multi-site workflows, you will need a :ref:`Registry <registry>`
   and a :ref:`Workflow service <workflow>`.

.. raw:: html

   <hr>
