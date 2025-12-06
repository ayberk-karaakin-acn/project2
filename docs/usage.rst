Usage
=====

Basic Usage
-----------

Run the application:

.. code-block:: bash

   myapp

Run as a Python module:

.. code-block:: bash

   python -m myapp

Command-line Options
--------------------

Show version:

.. code-block:: bash

   myapp --version

Use custom configuration file:

.. code-block:: bash

   myapp --config config.yml

Enable verbose output:

.. code-block:: bash

   myapp --verbose

Set log level:

.. code-block:: bash

   myapp --log-level DEBUG

Write logs to file:

.. code-block:: bash

   myapp --log-file app.log

Show help:

.. code-block:: bash

   myapp --help

Configuration
-------------

YAML Configuration
~~~~~~~~~~~~~~~~~~

Create a ``config.yml`` file:

.. code-block:: yaml

   app:
     name: myapp
     version: 0.1.0

   logging:
     level: INFO
     format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

TOML Configuration
~~~~~~~~~~~~~~~~~~

Create a ``config.toml`` file:

.. code-block:: toml

   [app]
   name = "myapp"
   version = "0.1.0"

   [logging]
   level = "INFO"
   format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

Then use it:

.. code-block:: bash

   myapp --config config.yml
   # or
   myapp --config config.toml

Examples
--------

Example 1: Basic Run
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ myapp
   will be implemented

Example 2: With Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ myapp --config my_config.yml
   will be implemented

Example 3: Verbose Mode
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ myapp --verbose
   INFO: Starting MyApp
   INFO: MyApp completed successfully
   will be implemented


