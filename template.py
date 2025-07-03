# Importing the built-in `os` module to interact with the operating system (e.g., file system operations)
import os

# Importing `Path` from `pathlib` for modern and readable path handling
from pathlib import Path

# Importing logging module to display informative messages (like what files or folders are being created)
import logging

# Configuring the logging format and level (INFO level means general messages will be shown)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the list of file paths that need to be created for the project structure
list_of_files = [
    "src/_init_.py",            # Python package initializer (should be "__init__.py", not "_init_.py")
    "src/helper.py",            # Helper module to store utility functions
    "src/prompt.py",            # File to store prompt templates or logic
    ".env",                     # Environment file to store secrets like API keys
    "setup.py",                 # Python setup script for packaging the project
    "app.py",                   # Main application script (Streamlit or Flask, etc.)
    "research/trials.ipynb",    # Jupyter notebook for experiments or testing ideas
    "test.py"
]

# Loop through each file path in the list to create necessary directories and files
for file_path in list_of_files:
    file_path = Path(file_path)  # Convert the string path to a Path object (better handling)
    file_dir, file_name = os.path.split(file_path)  # Split the path into directory and filename

    # If there is a directory path (not just a filename), ensure the directory exists
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)  # Create the directory (and parents) if not already there
        logging.info(f'Creating directory: {file_dir} for the file: {file_name}')  # Log directory creation

    # If the file does not exist or is an empty file, create or overwrite it as an empty file
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:  # Open file in write mode to create an empty file
            pass  # Do nothing inside the file for now
        logging.info(f'Creating empty file: {file_path}')  # Log file creation
    else:
        logging.info(f'{file_name} already exists')  # If file exists and is not empty, log that it exists
