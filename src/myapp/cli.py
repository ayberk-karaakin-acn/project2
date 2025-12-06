"""Command-line interface for MyApp."""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional, Sequence

from . import __version__
from .core import run_application
from .config import setup_logging, load_config


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.
    
    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(
        prog="myapp",
        description="MyApp - An enterprise-level terminal application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  myapp --version
  myapp --config config.yml
  myapp --verbose

For more information, visit: https://github.com/yourusername/myapp
        """
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    
    parser.add_argument(
        "-c", "--config",
        type=Path,
        help="Path to configuration file (YAML or TOML)",
        metavar="FILE"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Set logging level (default: INFO)"
    )
    
    parser.add_argument(
        "--log-file",
        type=Path,
        help="Path to log file",
        metavar="FILE"
    )
    
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    Main entry point for the CLI application.
    
    Args:
        argv: Command-line arguments (defaults to sys.argv[1:])
        
    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else getattr(logging, args.log_level)
    setup_logging(level=log_level, log_file=args.log_file)
    logger = logging.getLogger(__name__)
    
    try:
        # Load configuration if provided
        config = {}
        if args.config:
            logger.info(f"Loading configuration from {args.config}")
            config = load_config(args.config)
        
        # Run the application
        logger.info("Starting MyApp")
        result = run_application(config)
        
        # Print result to terminal
        print(result)
        
        logger.info("MyApp completed successfully")
        return 0
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    except ValueError as e:
        logger.error(f"Invalid value: {e}")
        print(f"Error: {e}", file=sys.stderr)
        return 1
        
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        print(f"Error: An unexpected error occurred. Check logs for details.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())


