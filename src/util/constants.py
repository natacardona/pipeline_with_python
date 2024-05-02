import os


DATABASE = 'datachallenge'
DEFAULT_DATABASE = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DROP_DATABASE_COMMAND = "DROP DATABASE IF EXISTS {}"
CREATE_DATABASE_COMMAND = "CREATE DATABASE {}"
DATA_URL_LOCATION = "https://drive.google.com/uc?export=download&id=1ejZpGTvZa81ZGD7IRWjObFeVuYbsSvuB"
ROOT_DATA_DIRECTORY = "data"
CHILD_DATA_DIRECTORY = "raw"
 
DB_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'db.sql')