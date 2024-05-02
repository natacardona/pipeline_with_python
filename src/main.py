import psycopg2
import os
from psycopg2 import sql

def create_database():
    conn = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='postgres')
    conn.autocommit = True  
    cursor = conn.cursor()

    try:
        cursor.execute(sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier('datachallenge')))
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier('datachallenge')))
        print("Database created successfully")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def execute_sql_script(file_path):
    
    conn = psycopg2.connect(host='localhost', user='postgres', password='postgres', dbname='datachallenge')
    cursor = conn.cursor()
    
    with open(file_path, 'r') as file:
        sql_script = file.read()

    try:
        cursor.execute(sql_script)
        conn.commit()
        print("SQL script executed successfully")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_database()
    execute_sql_script(os.path.join(
    os.path.dirname(__file__), 'db.sql'))
