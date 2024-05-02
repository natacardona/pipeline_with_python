import os
import zipfile
import requests
import shutil

from util.constants import CHILD_DATA_DIRECTORY, DATA_URL_LOCATION, ROOT_DATA_DIRECTORY
from util.utils import ensure_directory_exists

def download_files():
    # Determine the base directory relatively from this file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    target_path = os.path.join(base_dir, ROOT_DATA_DIRECTORY, CHILD_DATA_DIRECTORY)
    # Ensure the directory exists
    ensure_directory_exists(target_path)
    
    local_filename = DATA_URL_LOCATION.split('=')[-1] + '.zip'
    path_to_file = os.path.join(target_path, local_filename)

    # Download the file
    response = requests.get(DATA_URL_LOCATION)
    response.raise_for_status()  # Will stop the script if the download fails

    # Save the file temporarily
    with open(path_to_file, 'wb') as f:
        f.write(response.content)

    # Extract the file and clean up
    extract_and_cleanup_zip(path_to_file, target_path)

def extract_and_cleanup_zip(zip_path, extract_to):
    """ Extracts a zip file and places all files directly into the target directory,
    ignoring any subdirectory structure in the zip file. """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract each file into the target directory
        for member in zip_ref.infolist():
            # Check if the member is a file
            if not member.filename.endswith('/'):
                # Define the target path for this file
                target_file_path = os.path.join(extract_to, os.path.basename(member.filename))
                # Extract the file to the target path
                source = zip_ref.open(member)
                target = open(target_file_path, 'wb')
                with source, target:
                    shutil.copyfileobj(source, target)

    # Remove the original zip file
    os.remove(zip_path)
