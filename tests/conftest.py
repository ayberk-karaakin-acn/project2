"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path
from typing import Dict, Any


@pytest.fixture
def sample_config() -> Dict[str, Any]:
    """
    Provide a sample configuration for testing.
    
    Returns:
        Dict[str, Any]: Sample configuration dictionary
    """
    return {
        "app": {
            "name": "myapp",
            "version": "0.1.0",
        },
        "logging": {
            "level": "DEBUG",
        }
    }


@pytest.fixture
def temp_config_file(tmp_path: Path) -> Path:
    """
    Create a temporary configuration file for testing.
    
    Args:
        tmp_path: Pytest temporary directory fixture
        
    Returns:
        Path: Path to temporary config file
    """
    config_file = tmp_path / "test_config.yml"
    config_content = """
app:
  name: myapp
  version: 0.1.0

logging:
  level: DEBUG
"""
    config_file.write_text(config_content)
    return config_file


@pytest.fixture
def temp_log_file(tmp_path: Path) -> Path:
    """
    Create a temporary log file path for testing.
    
    Args:
        tmp_path: Pytest temporary directory fixture
        
    Returns:
        Path: Path to temporary log file
    """
    return tmp_path / "test.log"


