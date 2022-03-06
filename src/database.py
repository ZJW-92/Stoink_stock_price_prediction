import pandas as pd
import sqlite3
from sqlite3 import Error


def db_connection(db):
    # Connect to database
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn

def create_table(db):

    # Connect to database
    conn = db_connection(db)
    # Create a cursor
    cursor = conn.cursor()

    # Create a table
    cursor.execute("""CREATE TABLE stocksdata (
        time text,
        open real,
        high real,
        low real,
        close real,
        volume integer
    );""")

    # Commit changes & close connection
    conn.commit()
    conn.close()

def show_table(db, name):

    conn = db_connection(db)
    cursor = conn.cursor()

    # Display columns
    print('\nColumns in Stocksdata table:')
    data=cursor.execute(f'''SELECT * FROM "{name}"''')
    for column in data.description:
        print(column[0])

    # Commit changes & close connection
    conn.commit()
    conn.close()

def drop_table(db, name):

    # # Connect to database
    conn = db_connection(db)
    # Create a cursor
    cursor = conn.cursor()

    # Drop table
    cursor.execute(f"DROP TABLE IF EXISTS {name}")

    print(f'{name} Table Dropped!')

    # Commit changes & close connection
    conn.commit()
    conn.close()

def load_database(db, csv, name):
    df = pd.read_csv(csv)

    print(df.dtypes)
    conn = db_connection(db)
    df.to_sql(name=f'{name}', con=conn, if_exists='replace')

def show_all(db):
    # Connect to database
    conn = db_connection(db)
    # Create a cursor
    cursor = conn.cursor()

    # Query the database
    # cursor.execute(f"SELECT * FROM '{name}'")
    cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table'")
    items = cursor.fetchall()

    for row in items:
        # for column in row:
        #     print("----------------------------")
        #     print(column)
        print("----------------------------")
        print(row)
    
    # Commit changes & close connection
    conn.commit()
    conn.close()

def query_stocks(db, table, symbol):
    # Connect to database
    conn = db_connection(db)
    # Create a cursor
    cursor = conn.cursor()

    # Query the database
    # cursor.execute(f"SELECT * FROM '{name}'")
    # cursor.execute(f"SELECT * FROM EARNINGS WHERE symbol='AAPL' LIMIT 1")
    cursor.execute(f"SELECT * FROM {table} WHERE symbol='{symbol}' GROUP BY symbol")
    items = cursor.fetchall()


    for row in items:
        print(row)
    
    # Commit changes & close connection
    conn.commit()
    conn.close()
