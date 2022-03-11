.. _tsi-building:

This is the UNICORE TSI server, used to interface to a batch sub
system such as Slurm.

Building
========

Use the supplied ``Makefile`` to run tests and/or build packages for
the various supported batch systems.

You will need Java, Maven and Ant to build HTML/PDF
documentation and RPM/DEB packages.

Packaging
---------

Run

.. code:: console

  $ make <bss>-<type>

where <bss> is one of: ``nobatch``, ``torque``, ``slurm``, ``lsf``
and <type> is one of: ``tgz``, ``deb``, ``rpm``.


Generic binary TGZ
------------------

To create a "generic" binary archive that can be used to install
any version of the TSI via the ``Install.sh`` script, run

.. code:: console

  $ make clean tgz


Generating the documentation
----------------------------

Run

.. code:: console

  $ make doc-generate

to create the HTML and PDF manuals.

.. code:: console

  $ make doc-deploy

to upload to ``unicore-dev`` server

or just

.. code:: console

  $ make doc

to do both.
