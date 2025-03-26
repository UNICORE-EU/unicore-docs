.. _rest-api-examples-job:

|job-desc-img| Job submission and management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |job-desc-img| image:: ../../_static/job-desc.png
	:height: 32px
	:align: middle

.. code:: python

	#!/usr/bin/env python3

	import json
	import pyunicore.client as uc_client
	import pyunicore.credentials as uc_credentials

	# Base URL
	base = "https://localhost:8080/DEMO-SITE/rest/core"
	print ("Accessing REST API at ", base)

	#
	# setup authentication using username and password
	#
	credentials = uc_credentials.UsernamePassword("demouser", "test123")

	#
	# Create a client
	#
	site_client = uc_client.Client(credentials, base)
	
	#
	# Run a test job
	#
	job_description = {'Executable': "/bin/ls", 'Arguments' :["-lisa", "$HOME"], }

	job = site_client.new_job(job_description)
	print("Submitted: %s" % job)

	# let's wait while the job is still running
	job.poll()

	# print job properties
	print (json.dumps(job.properties, sort_keys=True, indent=4))

	# Accessing job outputs

	# We can access the wob working directory and the stdout/stderr files 

	working_dir = job.working_dir
	print (json.dumps(working_dir.properties, sort_keys=True, indent=4))

	# Let's list all files in the working directory

	for f in working_dir.listdir("."):
		print(f)

	# Now let's download data from the 'stdout' file
	stdout_content = working_dir.stat("stdout").raw().readlines()
	for line in stdout_content:
		print(line)


.. raw:: html

   <hr>
