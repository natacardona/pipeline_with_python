import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from hashlib import sha256

def compute_hash(row):
    """Compute a SHA-256 hash of the given row."""
    row_str = ''.join(map(str, row.values))
    return sha256(row_str.encode()).hexdigest()

def load_data_to_db(file_path, engine,display_stats=False):
    # Load CSV data into DataFrame
    data = pd.read_csv(file_path)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    if not data.empty:
        # Compute hash for each row
        data['row_hash'] = data.apply(compute_hash, axis=1)
        
        # Check for existing hashes
        existing_hashes = pd.read_sql('SELECT row_hash FROM transactions', session.bind)['row_hash'].tolist()

        # Filter out existing records based on hash
        data = data[~data['row_hash'].isin(existing_hashes)]

        if not data.empty:
            # Insert new records into the database
            data.to_sql('transactions', con=session.bind, if_exists='append', index=False)
            session.commit()
            print("New data inserted successfully.")
            
            # Calculate statistics
            total_rows = len(data)
            average_price = data['price'].mean() if not data['price'].isnull().all() else 0
            min_price = data['price'].min() if not data['price'].isnull().all() else 0
            max_price = data['price'].max() if not data['price'].isnull().all() else 0

            # Creating a DataFrame to hold the calculated values
            summary_data = {
                'Metric': ['Total Rows', 'Average Price', 'Minimum Price', 'Maximum Price'],
                'Value': [total_rows, average_price, min_price, max_price]
            }
            summary_df = pd.DataFrame(summary_data)

            print(summary_df)
            session.execute(
                text("""
                    INSERT INTO statistics (total_rows, average_price, min_price, max_price)
                    VALUES (:total_rows, :average_price, :min_price, :max_price)
                """),
                {'total_rows': total_rows, 'average_price': float(average_price), 'min_price': float(min_price), 'max_price': float(max_price)}
            )
            session.commit()
            
            print("Statistics inserted successfully.")
            if display_stats:
                print("\nCurrent Statistics for this file:")
                print(f"Total Rows: {total_rows}, Average Price: {average_price}, Minimum Price: {min_price}, Maximum Price: {max_price}")
        else:
            print("No new data to process.")
    else:
        print(f"No data found in {file_path}")
    session.close()         

def display_total_statistics(engine):
    print("----------------------------------------------------------------")
    query = """SELECT sum(total_rows) AS total_rows , sum(average_price) AS average_price , sum(min_price) AS min_price, sum(max_price) AS max_price FROM public.statistics;"""
    df = pd.read_sql(query, engine)
    print(df)
                  
def main():
    DATABASE = 'datachallenge'
    USER = 'postgres'
    PASSWORD = 'postgres'
    HOST = 'localhost'
    PORT = '5432'
    
    # Create a connection to the database
    engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

    # Get the base directory of the project
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    
    # Define the directory where CSV files are stored
    data_directory = os.path.join(base_dir, 'data', 'raw')

    # List of CSV files to process
    csv_files = ['2012-1.csv', '2012-2.csv', '2012-3.csv', '2012-4.csv', '2012-5.csv']
    
    # Process each CSV file
    for file_name in csv_files:
        file_path = os.path.join(data_directory, file_name)
        load_data_to_db(file_path, engine)
    
    display_total_statistics(engine)
    
     # Process the validation.csv file and display its statistics
    validation_file = os.path.join(data_directory, 'validation.csv')
    load_data_to_db(validation_file, engine, display_stats=True)   

if __name__ == "__main__":
    main()
