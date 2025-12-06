"""Tests for CLI module."""

import pytest
from pathlib import Path
from io import StringIO
import sys

from myapp.cli import create_parser, main
from myapp.core import run_application


class TestArgumentParser:
    """Tests for argument parser."""
    
    def test_parser_creation(self):
        """Test that parser is created successfully."""
        parser = create_parser()
        assert parser is not None
        assert parser.prog == "myapp"
    
    def test_version_argument(self):
        """Test --version argument."""
        parser = create_parser()
        with pytest.raises(SystemExit):
            parser.parse_args(["--version"])
    
    def test_config_argument(self):
        """Test --config argument."""
        parser = create_parser()
        args = parser.parse_args(["--config", "test.yml"])
        assert args.config == Path("test.yml")
    
    def test_verbose_argument(self):
        """Test --verbose argument."""
        parser = create_parser()
        args = parser.parse_args(["--verbose"])
        assert args.verbose is True
    
    def test_log_level_argument(self):
        """Test --log-level argument."""
        parser = create_parser()
        args = parser.parse_args(["--log-level", "DEBUG"])
        assert args.log_level == "DEBUG"
    
    def test_default_arguments(self):
        """Test default argument values."""
        parser = create_parser()
        args = parser.parse_args([])
        assert args.config is None
        assert args.verbose is False
        assert args.log_level == "INFO"


class TestMainFunction:
    """Tests for main CLI function."""
    
    def test_main_success(self, capsys):
        """Test successful execution of main function."""
        exit_code = main([])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "will be implemented" in captured.out
    
    def test_main_with_verbose(self, capsys):
        """Test main function with verbose flag."""
        exit_code = main(["--verbose"])
        assert exit_code == 0
    
    def test_main_with_nonexistent_config(self, capsys):
        """Test main function with non-existent config file."""
        exit_code = main(["--config", "nonexistent.yml"])
        captured = capsys.readouterr()
        assert exit_code == 1
        assert "Error" in captured.err or "Error" in captured.out
    
    def test_main_with_valid_config(self, temp_config_file, capsys):
        """Test main function with valid config file."""
        exit_code = main(["--config", str(temp_config_file)])
        captured = capsys.readouterr()
        assert exit_code == 0
        assert "will be implemented" in captured.out


class TestCoreFunction:
    """Tests for core application logic."""
    
    def test_run_application_no_config(self):
        """Test run_application with no configuration."""
        result = run_application()
        assert result == "will be implemented"
    
    def test_run_application_with_config(self, sample_config):
        """Test run_application with configuration."""
        result = run_application(sample_config)
        assert result == "will be implemented"
    
    def test_run_application_with_empty_config(self):
        """Test run_application with empty configuration."""
        result = run_application({})
        assert result == "will be implemented"


