#!/usr/bin/env python3
"""Build script for creating standalone executable using PyInstaller.

This script builds a standalone executable for the myapp application.
The executable can be distributed without requiring Python installation.

Usage:
    python scripts/build_exe.py
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def get_project_root() -> Path:
    """
    Get the project root directory.
    
    Returns:
        Path: Project root directory
    """
    return Path(__file__).parent.parent


def clean_build_dirs(project_root: Path) -> None:
    """
    Clean previous build directories.
    
    Args:
        project_root: Project root directory
    """
    dirs_to_clean = ["build", "dist"]
    
    for dir_name in dirs_to_clean:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"Cleaning {dir_name}/ directory...")
            shutil.rmtree(dir_path)


def create_spec_file(project_root: Path) -> Path:
    """
    Create PyInstaller spec file if it doesn't exist.
    
    Args:
        project_root: Project root directory
        
    Returns:
        Path: Path to spec file
    """
    spec_file = project_root / "myapp.spec"
    
    if not spec_file.exists():
        print("Creating PyInstaller spec file...")
        
        spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/myapp/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['myapp', 'myapp.cli', 'myapp.core', 'myapp.config'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='myapp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
        spec_file.write_text(spec_content)
        print(f"Created spec file: {spec_file}")
    
    return spec_file


def build_executable(project_root: Path, spec_file: Path) -> bool:
    """
    Build the executable using PyInstaller.
    
    Args:
        project_root: Project root directory
        spec_file: Path to spec file
        
    Returns:
        bool: True if build succeeded, False otherwise
    """
    print("\nBuilding executable with PyInstaller...")
    print("This may take a few minutes...\n")
    
    try:
        subprocess.run(
            ["pyinstaller", "--clean", str(spec_file)],
            cwd=project_root,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error building executable: {e}")
        return False
    except FileNotFoundError:
        print("Error: PyInstaller not found. Please install it:")
        print("  pip install pyinstaller")
        return False


def verify_executable(project_root: Path) -> bool:
    """
    Verify that the executable was created.
    
    Args:
        project_root: Project root directory
        
    Returns:
        bool: True if executable exists, False otherwise
    """
    if sys.platform == "win32":
        exe_path = project_root / "dist" / "myapp.exe"
    else:
        exe_path = project_root / "dist" / "myapp"
    
    if exe_path.exists():
        print(f"\n✓ Successfully built executable: {exe_path}")
        print(f"  Size: {exe_path.stat().st_size / (1024*1024):.2f} MB")
        return True
    else:
        print(f"\n✗ Executable not found: {exe_path}")
        return False


def main() -> int:
    """
    Main build function.
    
    Returns:
        int: Exit code
    """
    print("=" * 70)
    print("MyApp Executable Builder")
    print("=" * 70)
    
    project_root = get_project_root()
    print(f"\nProject root: {project_root}")
    
    # Clean previous builds
    clean_build_dirs(project_root)
    
    # Create spec file
    spec_file = create_spec_file(project_root)
    
    # Build executable
    success = build_executable(project_root, spec_file)
    
    if not success:
        print("\n✗ Build failed!")
        return 1
    
    # Verify executable
    if not verify_executable(project_root):
        print("\n✗ Verification failed!")
        return 1
    
    print("\n" + "=" * 70)
    print("Build completed successfully!")
    print("=" * 70)
    print("\nYou can now distribute the executable from the dist/ directory.")
    print("The executable is standalone and does not require Python.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())


