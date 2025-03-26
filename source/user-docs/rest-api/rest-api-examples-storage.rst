.. _rest-api-examples-storage:

|data-img| Storages and data management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. |data-img| image:: ../../_static/data-management.png
	:height: 32px
	:align: middle

.. code:: python

	#!/usr/bin/env python3

    import json, time
    import pyunicore.client as uc_client
    import pyunicore.credentials as uc_credentials

    # Base URL
    base = "https://localhost:8080/DEMO-SITE/rest/core"
    print ("Accessing REST API at ", base)
    # setup authentication using username and password
    credentials = uc_credentials.UsernamePassword("demouser", "test123")
    # Create a client
    site_client = uc_client.Client(credentials, base)

    # List storages
    all_storages = site_client.get_storages()
    for storage in all_storages:
        print(storage)

    # create two storages for testing
    storage  = site_client.new_job({}).working_dir
    storage2 = site_client.new_job({}).working_dir

    # storage properties
    print (json.dumps(storage.properties, sort_keys=True, indent=4))

    # upload some data
    storage.upload("test.txt", destination="test.txt")

    # List all files 
    for f in storage.listdir("."):
            print(f)

    # Access a file
    test_file = storage.stat("test.txt")
    print (json.dumps(test_file.properties, sort_keys=True, indent=4))

    # Download data from that file
    file_content = test_file.raw().readlines()
    for line in file_content:
            print(line)

    # server-server copy: "storage2" pulls file from "storage"
    source = storage._to_file_url("test.txt")
    print("Source file URL: "+source)
    transfer = storage2.receive_file(source, "copied-test.txt")
    while transfer.is_running():
        time.sleep(1)
    print (json.dumps(transfer.properties, sort_keys=True, indent=4))

    # Access copied file
    copied_file = storage2.stat("copied-test.txt")
    print (json.dumps(copied_file.properties, sort_keys=True, indent=4))


.. raw:: html

   <hr>
