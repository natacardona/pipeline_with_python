import os
import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db(file_path, engine):

    data = pd.read_csv(file_path)

    data.to_sql('transactions', con=engine, if_exists='append', index=False)
    print(f"data loaded from {file_path}")

def main():

    DATABASE = 'datachallenge'
    USER = 'postgres'
    PASSWORD = 'postgres'
    HOST = 'localhost'
    PORT = '5432'
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')


    data_directory = '/Users/cardonita/Documents/Development/etl_project/data/raw/dataPruebaDataEngineer'


    csv_files = ['2012-1.csv', '2012-2.csv', '2012-3.csv', '2012-4.csv', '2012-5.csv'] 
    for file_name in csv_files:
        file_path = os.path.join(data_directory, file_name)
        load_data_to_db(file_path, engine)

if __name__ == "__main__":
    main()
