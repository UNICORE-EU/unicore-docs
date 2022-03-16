.. _rest-api-examples-job:

Job submission and management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List of all examples :ref:`rest-api-examples`

.. code:: python

	#!/usr/bin/env python

	# Basic setup (URL etc)

	import requests
	import json
	import time

	base = "https://localhost:8080/DEMO-SITE/rest/core"
	print "Accessing REST API at ", base

	#
	# setup simple auth using username and password
	#
	credentials=("demouser","test123")

	#
	# check that we can access the server
	#
	headers = {'Accept': 'application/json'}
	r = requests.get(base, auth=credentials, headers=headers, verify=False)
	if r.status_code!=200:
		print "Error accessing the server!"
	else:
		print "Ready."
	print json.dumps(r.json(), indent=4)

	#
	# Run a simple test job
	#
	job = {'Executable': "/bin/ls", 'Arguments' :["-lisa", "$HOME"], }

	headers = {'content-type': 'application/json'}

	r = requests.post(base+"/jobs",data=json.dumps(job), headers=headers, auth=credentials, verify=False)
	print r.status_code
	if r.status_code!=201:
		print "Error submitting job:",
	else:
		jobURL = r.headers['Location']
		print "Submitted new job at",jobURL

	#
	# List our jobs (and their properties)
	#

	headers = {'Accept': 'application/json'}
	r = requests.get(base+"/jobs", headers=headers, auth=credentials, verify=False)
	jobList = r.json()
	print json.dumps(jobList, indent=4)

	#
	# Get the job properties
	#

	# first let's wait while the job is still running

	while True:
			headers = {'Accept': 'application/json'}
			r = requests.get(jobURL, headers=headers, auth=credentials, verify=False)
			jobProperties = r.json()
			jobStatus = jobProperties['status']
			print "Job is %s" % jobStatus
			if "SUCCESSFUL" == jobStatus:
					break
			time.sleep(10)

	# print job properties
	print json.dumps(jobProperties, sort_keys=True, indent=4)

	# Accessing job outputs

	# We can access the wob working directory and the stdout/stderr files 
	# in it. Note the use of links to point to interesting other resources.

	workingDir = jobProperties['_links']['workingDirectory']['href']
	r = requests.get(workingDir, headers=headers, auth=credentials, verify=False)
	workingDirProperties=r.json()
	print json.dumps(workingDirProperties, sort_keys=True, indent=4)

	# Let's list the files

	files = workingDirProperties['_links']['files']['href']
	r = requests.get(files, headers=headers, auth=credentials, verify=False)
	fileList=r.json()
	print json.dumps(fileList, sort_keys=True, indent=4)

	# Now let's download 'stdout'. Using "Accept: application/octet-stream" 
	# will download the data, otherwise we would get file info.

	headers = {'Accept': 'application/json'}
	r = requests.get(files+"/stdout", headers=headers, auth=credentials, verify=False)
	print json.dumps(r.json(), sort_keys=True, indent=4)

	headers = {'Accept': 'application/octet-stream'}
	r = requests.get(files+"/stdout", headers=headers, auth=credentials, verify=False)
	print "Job output:"
	print r.content
