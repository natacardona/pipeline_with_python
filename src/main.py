from db_creation import create_database, execute_sql_script
from extract.extract_data import download_files
from load.load_data import load_data

if __name__ == "__main__":
    create_database()
    execute_sql_script()
    download_files()
    load_data()