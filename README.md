# MyApp

An enterprise-level terminal application built with Python 3.12.

## Features

- 🚀 Modern CLI interface using argparse
- 📦 Proper packaging with pyproject.toml (PEP 621)
- 🧪 Comprehensive test suite with pytest
- 📝 Full documentation with Sphinx
- 🔧 Code quality tools (black, flake8, mypy, isort)
- 📊 Logging with rotating file handlers
- ⚙️ Configuration file support (YAML/TOML)
- 💾 Executable (.exe) build support with PyInstaller

## Installation

### Using Conda (Recommended)

1. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate myapp
```

2. Install the package in development mode:
```bash
pip install -e .
```

### Using pip

```bash
pip install -e .
```

### Install with development dependencies

```bash
pip install -e ".[dev,test]"
```

## Usage

After installation, you can run the application using:

```bash
myapp
```

Or as a Python module:

```bash
python -m myapp
```

### Command-line Options

```bash
# Show version
myapp --version

# Use custom configuration file
myapp --config config.yml

# Enable verbose output
myapp --verbose

# Set log level
myapp --log-level DEBUG

# Write logs to file
myapp --log-file app.log

# Show help
myapp --help
```

## Configuration

Create a configuration file (YAML or TOML format):

**config.yml:**
```yaml
app:
  name: myapp
  version: 0.1.0

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

**config.toml:**
```toml
[app]
name = "myapp"
version = "0.1.0"

[logging]
level = "INFO"
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=myapp

# Run specific test file
pytest tests/test_cli.py

# Run with verbose output
pytest -v
```

### Code Quality

```bash
# Format code with black
black src tests

# Check code style with flake8
flake8 src tests

# Type checking with mypy
mypy src

# Sort imports with isort
isort src tests

# Run all checks
black src tests && isort src tests && flake8 src tests && mypy src
```

### Building Documentation

```bash
cd docs
make html
```

View the documentation by opening `docs/_build/html/index.html` in your browser.

### Building Executable

To build a standalone executable:

```bash
python scripts/build_exe.py
```

The executable will be created in the `dist` directory.

On Windows, you can distribute the `.exe` file without requiring Python installation.

## Project Structure

```
project2/
├── src/
│   └── myapp/
│       ├── __init__.py          # Package initialization
│       ├── __main__.py          # Entry point for module execution
│       ├── cli.py               # CLI argument parser
│       ├── core.py              # Core business logic
│       └── config.py            # Configuration management
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── test_cli.py              # CLI tests
│   └── test_config.py           # Configuration tests
├── docs/
│   ├── conf.py                  # Sphinx configuration
│   ├── index.rst                # Documentation index
│   └── Makefile                 # Documentation build script
├── scripts/
│   └── build_exe.py             # PyInstaller build script
├── requirements/
│   ├── base.txt                 # Runtime dependencies
│   ├── dev.txt                  # Development dependencies
│   └── test.txt                 # Testing dependencies
├── environment.yml              # Conda environment
├── pyproject.toml               # Modern Python packaging
├── setup.py                     # Setuptools entry point
├── setup.cfg                    # Additional setup configuration
├── .gitignore                   # Git ignore patterns
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## Requirements

- Python 3.12+
- PyYAML >= 6.0
- colorama >= 0.4.6
- tomli >= 2.0.1 (for Python < 3.11)

## Development Requirements

- pytest >= 7.4
- pytest-cov >= 4.1
- black >= 23.0
- flake8 >= 6.0
- mypy >= 1.5
- isort >= 5.12
- sphinx >= 7.0
- pyinstaller >= 6.0

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Contact

Ayberk Karaakin - ayberk.karaakin@accenture.com

Project Link: [https://github.com/yourusername/myapp](https://github.com/yourusername/myapp)

## Acknowledgments

- Built with Python 3.12
- Uses argparse for CLI
- Packaged with setuptools
- Tested with pytest
- Documented with Sphinx

