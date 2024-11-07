import os
import psycopg2
from psycopg2 import sql

# Function to connect to PostgreSQL database 
def connect_db():
    # Retrieve the PostgreSQL URL from environment variable
    postgres_url = os.getenv('POSTGRES_URL')
    
    if not postgres_url:
        raise ValueError("POSTGRES_URL is not set in the environment variables")

    # Connect to PostgreSQL using psycopg2
    conn = psycopg2.connect(postgres_url)
    return conn

# Creating tables
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create stock table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock (
        name TEXT PRIMARY KEY,
        quantity INTEGER NOT NULL
    )
    ''')

    # Create selling_prices table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS selling_prices (
        name TEXT PRIMARY KEY,
        price REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

# Create the table if it doesn't exist when this module is imported
create_table()
