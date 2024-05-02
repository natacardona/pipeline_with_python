from hashlib import sha256
import os

def ensure_directory_exists(directory):
    """ Ensure the directory exists, and if not, create it. """
    if not os.path.exists(directory):
        os.makedirs(directory)

def compute_hash(row):
    """Compute a SHA-256 hash of the given row."""
    row_str = ''.join(map(str, row.values))
    return sha256(row_str.encode()).hexdigest()