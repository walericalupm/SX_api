from app import app
from flask import request
import constants as uri
from queries import create_product


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test', methods=['POST'])
def test():
    data = request.json
    return 'Hello ' + data['nombre']


@app.route(uri.BASE_URL_V1 + uri.PRODUCTS, methods=['POST'])
def create_product_api():
    dto_product = request.json
    if create_product(dto_product):
        return "product created"
    else:
        return "error creating product"
