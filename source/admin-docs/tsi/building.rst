.. _tsi-building:


Building
========

Clone the git repository

.. code:: console

  $ git clone https://github.com/UNICORE-EU/tsi
  $ cd tsi


Use the supplied ``Makefile`` to run tests and/or build packages for
the various supported batch systems.

You will need Java, Maven and Ant to build RPM/DEB packages.

Packaging
---------

Run

.. code:: console

  $ make <bss>-<type>

where <bss> is one of: ``nobatch``, ``slurm``, ``torque``, ``lsf``
and <type> is one of: ``tgz``, ``deb``, ``rpm``.


Generic binary TGZ
------------------

To create a "generic" binary archive that can be used to install
any version of the TSI via the ``Install.sh`` script, run

.. code:: console

  $ make clean tgz

