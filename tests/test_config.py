"""Tests for configuration module."""

import pytest
import logging
from pathlib import Path

from myapp.config import setup_logging, load_config, get_default_config


class TestLogging:
    """Tests for logging setup."""
    
    def test_setup_logging_default(self):
        """Test default logging setup."""
        setup_logging()
        logger = logging.getLogger()
        assert logger.level == logging.INFO
    
    def test_setup_logging_with_level(self):
        """Test logging setup with custom level."""
        setup_logging(level=logging.DEBUG)
        logger = logging.getLogger()
        assert logger.level == logging.DEBUG
    
    def test_setup_logging_with_file(self, temp_log_file):
        """Test logging setup with log file."""
        setup_logging(log_file=temp_log_file)
        assert temp_log_file.exists()


class TestConfigLoading:
    """Tests for configuration loading."""
    
    def test_load_yaml_config(self, temp_config_file):
        """Test loading YAML configuration."""
        config = load_config(temp_config_file)
        assert isinstance(config, dict)
        assert "app" in config
    
    def test_load_nonexistent_config(self):
        """Test loading non-existent configuration file."""
        with pytest.raises(FileNotFoundError):
            load_config(Path("nonexistent.yml"))
    
    def test_load_unsupported_format(self, tmp_path):
        """Test loading unsupported configuration format."""
        config_file = tmp_path / "test.ini"
        config_file.write_text("[section]\nkey=value")
        with pytest.raises(ValueError):
            load_config(config_file)
    
    def test_get_default_config(self):
        """Test getting default configuration."""
        config = get_default_config()
        assert isinstance(config, dict)
        assert "app" in config
        assert "logging" in config

