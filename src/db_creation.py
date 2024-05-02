import psycopg2
from util.constants import *
from psycopg2 import sql

def create_database():
    conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DEFAULT_DATABASE)
    conn.autocommit = True  
    cursor = conn.cursor()

    try:
        cursor.execute(sql.SQL(DROP_DATABASE_COMMAND).format(sql.Identifier(DATABASE)))
        cursor.execute(sql.SQL(CREATE_DATABASE_COMMAND).format(sql.Identifier(DATABASE)))
    except psycopg2.Error as e:
        exit(1)
    finally:
        cursor.close()
        conn.close()

def execute_sql_script():
    
    conn = psycopg2.connect(host=HOST, user=USER, password=PASSWORD, dbname=DATABASE)
    cursor = conn.cursor()
    
    with open(DB_SCRIPT_PATH, 'r') as file:
        sql_script = file.read()

    try:
        cursor.execute(sql_script)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
