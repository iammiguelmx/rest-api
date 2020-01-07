from flask import Flask, jsonify, request
from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_product
from dbutils import db_find_one
from dbutils import db_update_one
from dbutils import db_find_all
from dbutils import db_delete_one

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

# List All Data Route
@app.route('/products', methods=['GET'])
def showProducts():
    output = []
    for p in db_find_all(products):
        output.append(
            {
            'name' : p['name'], 
            'price' : p['price'],
            'quantity' : p['quantity']
            }
        )
    return jsonify(
        {
            'Products' : output
        }
    )

# Get by name Data Route
@app.route('/products/<string:name>', methods=['GET']) 
def getProduct(name):
    query = db_find_one(products, {'name': name})
    if query:
        output = {
            'name': query['name'],
            'price': query['price'],
            'quantity': query['quantity']
            }
    else:
        output = "No such name"
    return jsonify(
        {
            'Product' : output    
        }
    )

# Delete by Name Data Route
@app.route('/products/<string:name>', methods=['DELETE']) 
def deleteProduct(name):
    query = db_delete_one(products, {'name': name})
    return jsonify(
        {
            'status': 200,
            'message': 'Product Delete '  
        }
    )

# Update Data Route
@app.route('/products/<string:name>', methods=['PUT'])
def editProduct(name):
    return jsonify(
        {
            'status': 200,
            'mesagge': 'Updated'
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