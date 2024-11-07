# database.py

import sqlite3

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('stock.db')
    return conn

# creating tables
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock (
                        name TEXT PRIMARY KEY,
                        quantity INTEGER NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS selling_prices (
                        name TEXT PRIMARY KEY,
                        price REAL NOT NULL
                    )''')
    conn.commit()
    conn.close()





    

# Create the table if it doesn't exist when this module is imported
create_table()
