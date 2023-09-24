from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import json

import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

#Passes ID and edits details of a product
@app.route('/editProduct', methods=['POST', 'GET'])
def edit_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.edit_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#Inserts new UOM
@app.route('/insertUOM', methods=['POST'])
def insert_uom():
    request_payload = json.loads(request.form['data'])
    uom_id = uom_dao.insert_new_uom(connection, request_payload)
    response = jsonify({
        'uom_id': uom_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#Order details (customer_name, product, quantity, total_price)
# of a particular order is fetched from the Database
@app.route('/getOrderDetails', methods=['POST'])
def get_order_details():
    response =orders_dao.get_order_details(connection, request.form['order_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    products = orders_dao.get_all_orders(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":

    print("Starting Python Flash Server For Grocery Store Management System")
    app.run(port=5000)

# sayfayı görüntüleyebilmek için tarayıcıya -> http://127.0.0.1:5000/


