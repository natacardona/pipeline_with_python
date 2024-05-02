import os


DATABASE = 'datachallenge'
DEFAULT_DATABASE = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
PORT = '5432'
DROP_DATABASE_COMMAND = "DROP DATABASE IF EXISTS {}"
CREATE_DATABASE_COMMAND = "CREATE DATABASE {}"

 
DB_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'db.sql')