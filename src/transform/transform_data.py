import os
import zipfile
import requests

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

    with open(path_to_file, 'wb') as f:
        f.write(response.content)
        print(f"File saved to: {path_to_file}")

    if local_filename.endswith('.zip'):
        with zipfile.ZipFile(path_to_file, 'r') as zip_ref:
            zip_ref.extractall(target_path)
            print(f"File extracted in {target_path}")

# URL of the file you want to download
url = 'https://drive.google.com/uc?export=download&id=1ejZpGTvZa81ZGD7IRWjObFeVuYbsSvuB'

# Local path where you want to save the downloaded file
base_dir = '../../'
extract_to = os.path.join(base_dir, 'data', 'raw')

download_file(url, extract_to)
