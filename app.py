from flask import Flask, render_template, request, redirect, url_for
import database_config.stock_managment_db as stock_db
import database_config.selling_prices_db as selling_price_db


app = Flask(__name__)


# Define routes
@app.route("/")
def index():
    return render_template('index.html')



# stock management routes
@app.route('/stock_managment')
def stock_managment():
    stock_list = stock_db.view_stock()
    return render_template('stock_managment.html', stock_list=stock_list)

@app.route('/add', methods=['POST'])
def add_stock():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        stock_db.add_stock(name, quantity)
    return redirect(url_for('stock_managment'))

@app.route('/deduct', methods=['POST'])
def deduct_stock():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        stock_db.deduct_stock(name, quantity)
    return redirect(url_for('stock_managment'))



@app.route('/delete/<name>', methods=['GET'])
def delete_stock(name):
    stock_db.delete_stock(name)
    selling_price_db.delete_selling_prices(name)
    return redirect(url_for('stock_managment'))




#selling price routes
@app.route('/selling_prices')
def show_selling_prices():
    selling_price_db.add_product_name()
    # Retrieve stock list from the database
    prices_list = selling_price_db.show_selling_prices()
    return render_template('selling_prices.html', prices_list=prices_list)

@app.route('/add_selling_prices', methods=['POST'])
def add_selling_prices():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        print(name, price)
        selling_price_db.add_selling_price(name, price)
    return redirect(url_for('show_selling_prices'))





if __name__ == '__main__':
    app.run(debug=True)
