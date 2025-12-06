.. MyApp documentation master file

Welcome to MyApp's documentation!
==================================

MyApp is an enterprise-level terminal application built with Python 3.12.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api
   contributing

Features
--------

* Modern CLI interface using argparse
* Proper packaging with pyproject.toml (PEP 621)
* Comprehensive test suite with pytest
* Full documentation with Sphinx
* Code quality tools (black, flake8, mypy, isort)
* Logging with rotating file handlers
* Configuration file support (YAML/TOML)
* Executable (.exe) build support with PyInstaller

Quick Start
-----------

Installation
~~~~~~~~~~~~

Using Conda (Recommended):

.. code-block:: bash

   conda env create -f environment.yml
   conda activate myapp
   pip install -e .

Using pip:

.. code-block:: bash

   pip install -e .

Basic Usage
~~~~~~~~~~~

.. code-block:: bash

   # Run the application
   myapp

   # Show help
   myapp --help

   # Use custom configuration
   myapp --config config.yml

   # Enable verbose output
   myapp --verbose

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

