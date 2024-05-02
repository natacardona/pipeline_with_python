import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from hashlib import sha256

from util.constants import CHILD_DATA_DIRECTORY, CSV_FILES, DATAFRAME_HEADERS, DB_ENGINE, INSERT_STATISTICS_QUERY, ROOT_DATA_DIRECTORY, SELECT_TRANSACTIONS_QUERY, STATISTICS_QUERY, VALIDATION_CSV_FILE

# Get the base directory of the project
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))    
# Define the directory where CSV files are stored
data_directory = os.path.join(base_dir, ROOT_DATA_DIRECTORY , CHILD_DATA_DIRECTORY)
# Define the directory where CSV files are stored
validation_file = os.path.join(data_directory, VALIDATION_CSV_FILE)
    
def compute_hash(row):
    """Compute a SHA-256 hash of the given row."""
    row_str = ''.join(map(str, row.values))
    return sha256(row_str.encode()).hexdigest()

def load_data_to_db(file_path, display_stats=False):
    # Load CSV data into DataFrame
    data = pd.read_csv(file_path)
    
    Session = sessionmaker(bind=DB_ENGINE)
    session = Session()
    
    if not data.empty:
        # Compute hash for each row
        data['row_hash'] = data.apply(compute_hash, axis=1)
        
        # Check for existing hashes
        existing_hashes = pd.read_sql(SELECT_TRANSACTIONS_QUERY, session.bind)['row_hash'].tolist()

        # Filter out existing records based on hash
        data = data[~data['row_hash'].isin(existing_hashes)]

        if not data.empty:
            # Insert new records into the database
            data.to_sql('transactions', con=session.bind, if_exists='append', index=False)
            session.commit()
            
            # Calculate statistics
            total_rows = len(data)
            average_price = data['price'].mean() if not data['price'].isnull().all() else 0
            min_price = data['price'].min() if not data['price'].isnull().all() else 0
            max_price = data['price'].max() if not data['price'].isnull().all() else 0

            # Creating a DataFrame to hold the calculated values
            summary_data = {
                'Metric': DATAFRAME_HEADERS,
                'Value': [total_rows, average_price, min_price, max_price]
            }
            summary_df = pd.DataFrame(summary_data)

            print("----------------------------------------------------------------")
            print(summary_df)
            print("----------------------------------------------------------------")
            
            session.execute(
                text(INSERT_STATISTICS_QUERY),
                {'total_rows': total_rows, 'average_price': float(average_price), 'min_price': float(min_price), 'max_price': float(max_price)}
            )
            session.commit()
            
            if display_stats:
                print("\nCurrent Statistics for this file:")
                print(f"Total Rows: {total_rows}, Average Price: {average_price}, Minimum Price: {min_price}, Maximum Price: {max_price}")
        else:
            pass
    else:
        print(f"No data found in {file_path}")
        pass
    session.close()         

def display_total_statistics():
    print("----------------------------------------------------------------")    
    df = pd.read_sql(STATISTICS_QUERY, DB_ENGINE)
    print(df)
                  
def load_data():
    
    # Process each CSV file
    for file_name in CSV_FILES:
        file_path = os.path.join(data_directory, file_name)
        load_data_to_db(file_path)
    
    display_total_statistics()
    # Process the validation.csv file and display its statistics        
    load_data_to_db(validation_file, display_stats=True)   
