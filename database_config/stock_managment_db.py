from .db_connection import *
import sqlite3

create_table()

def add_stock(name, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO stock (name, quantity) VALUES (?, ?)''', (name, quantity))
        conn.commit()
    except sqlite3.IntegrityError:
        cursor.execute('''SELECT * FROM stock WHERE name = ?''', (name,))
        pre_quan = cursor.fetchall()
        pre_quan = pre_quan[0]
        quantity = int(pre_quan[1]) + int(quantity)
        cursor.execute('''UPDATE stock SET quantity = ? WHERE name = ?''', (quantity, name))
        conn.commit()
    finally:
        conn.close()

# Function to update a stock item in the database
def update_stock(name, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''UPDATE stock SET quantity = ? WHERE name = ?''', (quantity, name))
    conn.commit()
    conn.close()

def deduct_stock(name, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM stock WHERE name = ?''', (name,))
    pre_quan = cursor.fetchall()
    pre_quan = pre_quan[0]
    quantity = int(pre_quan[1]) - int(quantity)
    cursor.execute('''UPDATE stock SET quantity = ? WHERE name = ?''', (quantity, name))
    conn.commit()
    conn.close()

# Function to delete a stock item from the database
def delete_stock(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM stock WHERE name = ?''', (name,))
    conn.commit()
    conn.close()

# Function to view all stock items in the database
# Function to view all stock items in the database
def view_stock():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM stock''')
    stock_list = cursor.fetchall()
    conn.close()
    print(stock_list)
    return stock_list