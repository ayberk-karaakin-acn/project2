# Quick Start Guide

This guide will help you get MyApp up and running in just a few minutes.

## 1. Setup Environment

Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate myapp
```

## 2. Install Package

Install the package in development mode:

```bash
pip install -e .
```

## 3. Run the Application

Simply run:

```bash
myapp
```

You should see:
```
will be implemented
```

## 4. Test the Application

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=myapp --cov-report=html
```

View coverage report by opening `htmlcov/index.html` in your browser.

## 5. Build Documentation

```bash
cd docs
make html
```

View the documentation by opening `docs/_build/html/index.html` in your browser.

## 6. Build Executable

To create a standalone executable:

```bash
python scripts/build_exe.py
```

The executable will be in the `dist/` directory.

## Development Workflow

### Format Code

```bash
black src tests
isort src tests
```

### Check Code Quality

```bash
flake8 src tests
mypy src
```

### Run All Checks

```bash
black src tests && isort src tests && flake8 src tests && mypy src && pytest
```

## Common Commands

| Task | Command |
|------|---------|
| Run app | `myapp` or `python -m myapp` |
| Show help | `myapp --help` |
| Show version | `myapp --version` |
| Verbose mode | `myapp --verbose` |
| With config | `myapp --config config.yml` |
| Run tests | `pytest` |
| Format code | `black src tests` |
| Check linting | `flake8 src tests` |
| Type check | `mypy src` |
| Build docs | `cd docs && make html` |
| Build exe | `python scripts/build_exe.py` |

## Next Steps

1. Replace the placeholder implementation in `src/myapp/core.py`
2. Add your business logic
3. Update tests in `tests/`
4. Update documentation in `docs/`
5. Customize configuration options
6. Add more CLI commands as needed

## Troubleshooting

### Issue: "command not found: myapp"

**Solution**: Make sure you've installed the package and activated the conda environment:
```bash
conda activate myapp
pip install -e .
```

### Issue: Import errors

**Solution**: Ensure all dependencies are installed:
```bash
pip install -e ".[dev,test]"
```

### Issue: PyInstaller build fails

**Solution**: Make sure PyInstaller is installed and you're in the project root:
```bash
pip install pyinstaller
cd /path/to/project2
python scripts/build_exe.py
```

## Project Structure Overview

```
project2/
├── src/myapp/          # Source code
├── tests/              # Test suite
├── docs/               # Documentation
├── scripts/            # Build scripts
├── requirements/       # Dependencies
├── environment.yml     # Conda environment
├── pyproject.toml      # Package configuration
└── README.md          # Full documentation
```

For more detailed information, see [README.md](README.md).


