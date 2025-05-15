import os
from typing import Any

def get_project_root() -> str:
    """Returns the absolute path to the project root directory"""
    current_dir = os.getcwd()
    while True:
        if all(os.path.isdir(os.path.join(current_dir, d)) for d in ["Pitt", "data"]):
            return current_dir
        parent = os.path.dirname(current_dir)
        if parent == current_dir:
            raise RuntimeError("Project root with 'Pitt/' and 'data/' folders not found.")
        current_dir = parent

PROJECT_ROOT = get_project_root()

def from_root(*parts : str) -> str:
    """Joins path parts to the project root"""
    return os.path.join(PROJECT_ROOT, *parts)