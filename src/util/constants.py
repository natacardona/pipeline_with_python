import os

from sqlalchemy import create_engine


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
DB_ENGINE = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
CSV_FILES = ['2012-1.csv', '2012-2.csv', '2012-3.csv', '2012-4.csv', '2012-5.csv']
DATAFRAME_HEADERS = ['Total Rows', 'Average Price', 'Minimum Price', 'Maximum Price']
INSERT_STATISTICS_QUERY = """ INSERT INTO statistics (total_rows, average_price, min_price, max_price) VALUES (:total_rows, :average_price, :min_price, :max_price) """
VALIDATION_CSV_FILE = 'validation.csv'
SELECT_TRANSACTIONS_QUERY = 'SELECT row_hash FROM transactions'
STATISTICS_QUERY = """SELECT sum(total_rows) AS total_rows , sum(average_price) AS average_price , sum(min_price) AS min_price, sum(max_price) AS max_price FROM public.statistics;"""
 
DB_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'db.sql')