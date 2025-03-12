.. _glossary:

Glossary
========

This page includes a number of terms that we use in our documentation,
so that you have a reference for how we're using them.

.. glossary::
	:sorted:
	
.. unicore-gs:
	
	UNICORE
		A European Federation Software Suite. `UNICORE <https://www.unicore.eu>`_ 
		(UNiform Interface to COmputing REsources) 
		offers a ready-to-run system including client and server software.
	
.. _ucc-gs:
	
	UNICORE Commandline Client
		A full featured :ref:`commandline client <ucc>` for UNICORE.
	
.. _rest-api-gs:
	
	REST API
		:ref:`REST-API <rest-api>` for the :ref:`UNICORE/X <unicorex-gs>` server (job submission 
		and management, data access and data transfer) and the :ref:`Workflow server <workflow-gs>` 
		(workflow submission and management).
	
.. _job-description-gs:
	
	Job description format
		The :ref:`job description <job-description>` format that allows you to specify the 
		application or executable you want to run, arguments and environment settings, any files 
		to stage in from remote servers and any result files to stage out.
	
.. _workflow-description_gs:
	
	Workflow description
		The :ref:`workflow description <workflow-description>` language that is supported by the 
		:ref:`Workflow engine <workflow-gs>`.
	
.. data-triggered-gs:
	
	Data-triggered processing
		Reference for the :ref:`data-triggered processing <data-triggered>` in 
		:ref:`UNICORE/X <unicorex-gs>`.
	
.. _uftpd-gs:
	
	UFTP Client
		The :ref:`UNICORE File Transfer Client <uftp-docs:uftp-client>` for high performance 
		data transfer.
	
.. _gateway-gs:
	
	Gateway
		A :ref:`Gateway <gateway>` server  is an optional component that provides a reverse 
		https proxy, allowing you to run several backend servers (:ref:`UNICORE/X <unicorex-gs>`, 
		:ref:`Registry <registry-gs>`, …) behind a single address.
	
.. _unicorex-gs:
	
	UNICORE/X
		The :ref:`UNICORE/X <unicorex>` is a central server of a typical UNICORE installation that 
		provides :ref:`REST-API <rest-api-gs>` for job management and data access services for a 
		single compute cluster (or just a file system).
	
.. _tsi-gs:
	
	TSI
		The :ref:`Target System Interface <tsi>` (TSI) server is used to interface to a resource 
		manager such as Slurm and to access files on the cluster.
	
.. _xuudb-gs:
	
	XUUDB
		An optional :ref:`XUUDB <xuudb>` service, that is best suited as a per-site service, 
		provids attributes for multiple :ref:`UNICORE/X <unicorex>`-like services at a site. 
		The XUUDB maps a UNICORE user identity (which is formally an X.500 distinguished 
		name (DN)) to a set of attributes which are typically used to provide local account details 
		(uid, gid(s)) and commonly also to provide authorization information, i.e. the user’s role.
	
.. _workflow-gs:
	
	Workflow Service
		:ref:`Workflow Service <workflow>` provides advanced workflow processing capabilities 
		using UNICORE resources. The Workflow service provides graphs of activities including 
		high-level control constructs (for-each, while, if-then-else, etc.), and submits and 
		manages the execution of single UNICORE jobs.
	
.. _registry-gs:
	
	Registry
		The :ref:`Registry <registry>` server is a specially configured :ref:`UNICORE/X <unicorex-gs>`
		server which provides the information about available services to clients and other 
		services.
	
.. uftpd-gs:
	
	UFTPD
		The :ref:`UNICORE File Transfer Server <uftp-docs:uftpd>` for high performance data 
		transfer.
	
.. _pyunicore-gs:
	
	pyUNICORE 
		`Python library <https://pyunicore.readthedocs.io/>`_ providing an API for UNICORE’s 
		:ref:`REST-API <rest-api-gs>`, making common tasks like file access, job submission and 
		management, workflow submission and management more convenient, and integrating UNICORE
		features better with typical Python usage.



