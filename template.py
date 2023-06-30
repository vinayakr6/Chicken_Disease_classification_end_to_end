import os
from pathlib import Path
import logging

# format for logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s') 

project_name = "cnnClassifier"

# List of files and folders to be created 
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]


for filepath in list_of_files:
    filepath = Path(filepath) # Path creates a windows path
    filedir, filename = os.path.split(filepath) # splits filepath into directories in the form of tuples


    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        # Logging message
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Creates an empty file if it doesn't exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    # gives a message file already exists
    else:
        logging.info(f"{filename} is already exists")

