import os

def get_project_root() -> str:
    """Returns the absolute path to the project root directory"""
    # quick utility to find root dir — assumes folder structure stays consistent 
    current_dir = os.getcwd()
    #TODO: make this more generalizable -> if they clone the repo they would have readme and data 
    markers = ['README.md', 'data']
    while True:
        all_markers_found = True
        for marker in markers:
            marker_path = os.path.join(current_dir, marker)
            if not os.path.exists(marker_path):
                all_markers_found = False
                break
        if all_markers_found:
            return current_dir
        parent = os.path.dirname(current_dir) # goes up 1 level
        if parent == current_dir:
            raise RuntimeError("Could not find project root dir")
        current_dir = parent

PROJECT_ROOT = get_project_root()

def from_root(*parts : str) -> str:
    """Joins path parts to the project root"""
    return os.path.join(PROJECT_ROOT, *parts)