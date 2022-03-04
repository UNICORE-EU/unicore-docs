.. _rest-api-examples-workflow:

Workflow submission and management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List of all examples :ref:`rest-api-examples`

We assume the reader knows how the :ref:`UNICORE Workflow system <workflow>` works, and has used 
it from a low-level tool such as :ref:`UCC <ucc>`.

.. code:: python

	#!/usr/bin/env python

	# Basic setup (URL etc)

	import requests
	import json
	import time

	requests.packages.urllib3.disable_warnings()

	base = "https://localhost:8080/WORKFLOW/rest/workflows"
	print "Accessing Workflow REST API at ", base

	#
	# setup simple auth using username and password
	#
	credentials=("demouser","test123")

	#
	# create the actual workflow
	#
	# https://unicore-dev.zam.kfa-juelich.de/documentation/workflow-8.0.0/workflow-manual.html#wf_dialect

	wf_json = {
		"activities": [
		   {
			  "id": "date1",
			  "job": {
				   "Executable": "date",
				   "Job type": "INTERACTIVE",
			  }
		  } 
		], 
	}

	#
	# post the workflow JSON to create a new 
	# workflow instance on the server
	#

	headers = {'Content-Type': 'application/json'}
	r = requests.post(base, data=wf_json, headers=headers, auth=credentials, verify=False)
	r.raise_for_status()

	workflow = r.headers['Location']

	# to see the workflow properties:
	headers = {'Accept': 'application/json'}
	r = requests.get(workflow, headers=headers, auth=credentials, verify=False)
	r.raise_for_status()
	print(r.json())
