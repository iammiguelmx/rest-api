from flask import Flask, jsonify, request
from products import products
from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_product
from dbutils import db_find_one
from dbutils import db_update_one

app = Flask(__name__)

# Inserta en la colletion de Productos
products = db_connect(MONGO_URI, 'mi_app', 'products')

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})


# Create Data Routes
@app.route('/products', methods=['POST'])
def addProduct():
    product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    db_insert_product(products, product)
    return jsonify(
        {
            'status': 200,
            'message': 'Successful ' 
        }
    )

# Update Data Route
@app.route('/products/<string:name>', methods=['PUT'])
def editProduct(name):
    # productsFound = [product for product in products if product['name'] == product_name]
    query = db_find_one(products, {'product': products._id})
    product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    db_update_one(products, product)
    return jsonify(
        {
        'status': 200,
        'message': 'Product Updated'
        }
    )


@app.errorhandler(404)
def not_found():
    message = {
        'status': 404,
        'message': 'Not Found ' 
    }
    response = jsonify(message)
    response.status_code = 404

    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)