from .db_connection import *
import sqlite3

create_table()

#adding product names to selling_prices table
def add_product_name():
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT * FROM stock''')
        stock_list = cursor.fetchall()
    except sqlite3.IntegrityError:
        print("stock table empty")
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
            cursor.execute('''INSERT INTO selling_prices (name, price) VALUES (?, ?)''', (name, price))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Product name already on table")
        finally:
            conn.close()


def add_selling_price(name, price):
    conn = connect_db()
    cursor = conn.cursor()
    # cursor.execute('''SELECT * FROM price_assign WHERE name = ?''', (name,))
    price = float(price)
    try:
        cursor.execute('''UPDATE selling_prices SET price = ? WHERE name = ?''', (price, name))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Product name already on table")
    finally:
        conn.close()


def show_selling_prices():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM selling_prices''')
    prices_list = cursor.fetchall()
    conn.close()
    return prices_list


def delete_selling_prices(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM selling_prices WHERE name = ?''', (name,))
    conn.commit()
    conn.close()
