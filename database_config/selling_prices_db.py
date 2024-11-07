from .db_connection import *
import psycopg2

# Create the tables if they don't exist
create_table()

# Adding product names to selling_prices table
def add_product_name():
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM stock')
        stock_list = cursor.fetchall()
    except psycopg2.DatabaseError as e:
        print("Error fetching data from stock table:", e)
        return
    finally:
        conn.close()

    print(stock_list)

    for rows in stock_list:
        price = 0
        name = rows[0]
        try:
            conn = connect_db()
            cursor = conn.cursor()
            price = float(price)
            cursor.execute('''
            INSERT INTO selling_prices (name, price) VALUES (%s, %s)
            ''', (name, price))
            conn.commit()
        except psycopg2.IntegrityError:
            print(f"Product name '{name}' already in the selling_prices table")
        finally:
            conn.close()

def add_selling_price(name, price):
    conn = connect_db()
    cursor = conn.cursor()
    price = float(price)
    
    try:
        cursor.execute('''
        UPDATE selling_prices SET price = %s WHERE name = %s
        ''', (price, name))
        conn.commit()
    except psycopg2.DatabaseError as e:
        print("Error updating selling price:", e)
    finally:
        conn.close()

def show_selling_prices():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM selling_prices')
    prices_list = cursor.fetchall()
    conn.close()
    return prices_list

def delete_selling_prices(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM selling_prices WHERE name = %s', (name,))
    conn.commit()
    conn.close()
