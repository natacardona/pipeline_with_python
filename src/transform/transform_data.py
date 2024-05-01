import os
import zipfile
import requests
import shutil

def ensure_directory_exists(directory):
    """ Ensure the directory exists, and if not, create it. """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created: {directory}")

def download_file(url, target_path):
    # Ensure the directory exists
    ensure_directory_exists(target_path)
    
    local_filename = url.split('=')[-1] + '.zip'
    path_to_file = os.path.join(target_path, local_filename)

    # Download the file
    response = requests.get(url)
    response.raise_for_status()  # Will stop the script if the download fails

    # Save the file temporarily
    with open(path_to_file, 'wb') as f:
        f.write(response.content)
        print(f"File saved to: {path_to_file}")

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
                print(f"Extracted {target_file_path}")

    # Remove the original zip file
    os.remove(zip_path)
    print(f"Zip file removed: {zip_path}")

# URL of the file you want to download
url = 'https://drive.google.com/uc?export=download&id=1ejZpGTvZa81ZGD7IRWjObFeVuYbsSvuB'

# Determine the base directory relatively from this file
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
extract_to = os.path.join(base_dir, 'data', 'raw')

# Download and extract the file
download_file(url, extract_to)
