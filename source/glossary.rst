.. _glossary:

Glossary
========

This page includes a number of terms that we use in our documentation,
so that you have a reference for how we're using them.

.. glossary::
	:sorted:
	

	UNICORE
		UNiform Interface to COmputing REsources
	
	UNICORE Commandline Client
		A full featured commandline client for UNICORE.

	REST API
		REST-API for the UNICORE/X server (job submission and management, data access and data transfer) 
		and the Workflow server (workflow submission and management).

	Job description format
		The job description format that allows you to specify the application or executable you want to run, 
		arguments and environment settings, any files to stage in from remote servers and any result files to stage out.

	Workflow description
		The workflow description language that is supported by the Workflow engine.

	Data-triggered processing
		Reference for the data-triggered processing in UNICORE/X.

	UFTP Client
		The UNICORE File Transfer Client for high performance data transfer.
		
	Gateway
		An optional server component that provides a reverse https proxy, 
		allowing you to run several backend servers (UNICORE/X, Registery, …) behind a single address.

	UNICORE/X
		The central server component of a typical UNICORE installation that provides 
		REST APIs for job management and data access services for a single compute cluster (or just a file system).

	TSI
		The Target System Interface (TSI) server is used to interface to a resource manager such 
		as Slurm and to access files on the cluster.

	XUUDB
		An optional service, that is best suited as a per-site service, providing attributes for multiple 
		UNICORE/X-like services at a site. The XUUDB maps a UNICORE user identity (which is formally 
		an X.500 distinguished name (DN)) to a set of attributes which are typically used to provide local account 
		details (uid, gid(s)) and commonly also to provide authorization information, i.e. the user’s role.

	Workflow Service
		Workflow Service provides advanced workflow processing capabilities using UNICORE resources. 
		The Workflow service provides graphs of activities including high-level control constructs 
		(for-each, while, if-then-else, etc.), and submits and manages the execution of single UNICORE jobs.

	Registry
		The Registry server is a specially configured UNICORE/X server which provides the information about 
		available services to clients and other services.

	UFTPD
		The UNICORE File Transfer Server for high performance data transfer.

	pyUNICORE 
		Python library providing an API for UNICORE’s REST API , making common tasks like file access, 
		job submission and management, workflow submission and management more convenient, and integrating UNICORE 
		features better with typical Python usage.



