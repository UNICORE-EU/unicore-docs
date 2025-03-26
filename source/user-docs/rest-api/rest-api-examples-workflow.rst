.. _rest-api-examples-workflow:

|workflow-img| Workflow submission and management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |workflow-img| image:: ../../_static/workflow.png
	:height: 32px
	:align: middle

.. code:: python

	#!/usr/bin/env python3

	import json
	import pyunicore.client as uc_client
	import pyunicore.credentials as uc_credentials

	base = "https://localhost:8080/WORKFLOW/rest/workflows"
	print ("Accessing Workflow REST API at ", base)

	#
	# setup authentication using username and password
	#
	credentials = uc_credentials.UsernamePassword("demouser", "test123")
	
	#
	# Create a client for the Workflow service
	#
	workflow_client = uc_client.WorkflowService(credentials, base)
	
	#
	# create the workflow description
	#

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
	# create a new workflow instance on the server
	#
	workflow = workflow_service.new_workflow(workflow_description)
	
	# see the workflow properties
	print (json.dumps(workflow.properties, sort_keys=True, indent=4))


.. raw:: html

   <hr>
