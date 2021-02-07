from app import app
from flask import request
from constants import *
from queries import create_product, update_product
from response import api_response, api_error_response


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test', methods=['POST'])
def test():
    data = request.json
    return 'Hello ' + data['nombre']


@app.route(BASE_URI_V1 + URI_PRODUCTS, methods=['POST'])
def create_product_api():
    dto_product = request.json
    code, product = create_product(dto_product)
    if code is CREATED or CONFLICT:
        return api_response(product.barcode,URI_PRODUCTS, code)
    else:
        return api_error_response(code)


@app.route(BASE_URI_V1 + URI_PRODUCTS + BARCODE_PARAM, methods=['PUT'])
def manage_product_by_barcode_api(barcode):
    dto_product = request.json
    if request.method == 'PUT':
        code, product = update_product(barcode, dto_product)
        if code is OK:
            return api_response(product.barcode, URI_PRODUCTS, code)
        else:
            return api_error_response(code)

