"""Configuration management for MyApp."""

import logging
import sys
from pathlib import Path
from typing import Dict, Any, Optional
from logging.handlers import RotatingFileHandler

try:
    import tomllib
except ImportError:
    import tomli as tomllib

import yaml


def setup_logging(
    level: int = logging.INFO,
    log_file: Optional[Path] = None,
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
) -> None:
    """
    Setup logging configuration with rotating file handler.
    
    Args:
        level: Logging level
        log_file: Path to log file (optional)
        max_bytes: Maximum size of log file before rotation
        backup_count: Number of backup files to keep
    """
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    # Clear existing handlers
    root_logger.handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # File handler (if log file is specified)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(log_format)
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)


def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Load configuration from a YAML or TOML file.
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Dict[str, Any]: Configuration dictionary
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config file format is not supported
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    suffix = config_path.suffix.lower()
    
    if suffix in (".yml", ".yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    
    elif suffix in (".toml",):
        with open(config_path, "rb") as f:
            return tomllib.load(f)
    
    else:
        raise ValueError(f"Unsupported configuration file format: {suffix}")


def get_default_config() -> Dict[str, Any]:
    """
    Get default configuration values.
    
    Returns:
        Dict[str, Any]: Default configuration
    """
    return {
        "app": {
            "name": "myapp",
            "version": "0.1.0",
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    }

