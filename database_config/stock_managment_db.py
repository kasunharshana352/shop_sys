from .db_connection import *
import psycopg2

# Create the tables if they don't exist
create_table()

def add_stock(name, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO stock (name, quantity) VALUES (%s, %s)
        ON CONFLICT (name) DO UPDATE SET quantity = stock.quantity + %s
        ''', (name, quantity, quantity))
        conn.commit()
    except psycopg2.DatabaseError as e:
        print("Error adding stock:", e)
    finally:
        conn.close()

def update_stock(name, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE stock SET quantity = %s WHERE name = %s
    ''', (quantity, name))
    conn.commit()
    conn.close()

def deduct_stock(name, quantity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM stock WHERE name = %s', (name,))
    pre_quan = cursor.fetchall()
    if pre_quan:
        pre_quan = pre_quan[0]
        quantity = int(pre_quan[1]) - int(quantity)
        cursor.execute('''
        UPDATE stock SET quantity = %s WHERE name = %s
        ''', (quantity, name))
        conn.commit()
    conn.close()

def delete_stock(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stock WHERE name = %s', (name,))
    conn.commit()
    conn.close()

def view_stock():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stock')
    stock_list = cursor.fetchall()
    conn.close()
    return stock_list
