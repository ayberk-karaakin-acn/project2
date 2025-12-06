Contributing
============

We welcome contributions to MyApp!

Development Setup
-----------------

1. Fork the repository
2. Clone your fork:

.. code-block:: bash

   git clone https://github.com/yourusername/myapp.git
   cd myapp

3. Create a conda environment:

.. code-block:: bash

   conda env create -f environment.yml
   conda activate myapp

4. Install in development mode:

.. code-block:: bash

   pip install -e ".[dev,test]"

Running Tests
-------------

Run all tests:

.. code-block:: bash

   pytest

Run with coverage:

.. code-block:: bash

   pytest --cov=myapp

Run specific test file:

.. code-block:: bash

   pytest tests/test_cli.py

Code Quality
------------

Format code with black:

.. code-block:: bash

   black src tests

Check code style with flake8:

.. code-block:: bash

   flake8 src tests

Type checking with mypy:

.. code-block:: bash

   mypy src

Sort imports with isort:

.. code-block:: bash

   isort src tests

Run all checks:

.. code-block:: bash

   black src tests && isort src tests && flake8 src tests && mypy src

Building Documentation
----------------------

.. code-block:: bash

   cd docs
   make html

View the documentation by opening ``docs/_build/html/index.html`` in your browser.

Submitting Changes
------------------

1. Create a feature branch:

.. code-block:: bash

   git checkout -b feature/amazing-feature

2. Make your changes and commit:

.. code-block:: bash

   git commit -m 'Add some amazing feature'

3. Push to your fork:

.. code-block:: bash

   git push origin feature/amazing-feature

4. Open a Pull Request

Code Style Guidelines
---------------------

* Follow PEP 8 style guide
* Use type hints for all function signatures
* Write docstrings for all public functions and classes
* Keep lines under 100 characters
* Write tests for new features
* Ensure all tests pass before submitting PR

