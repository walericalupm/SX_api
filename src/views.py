from src.app import app
from flask import request
from src.constants import *
from src.queries import create_product, update_product, get_product_by_barcode
from src.response import api_response, api_error_response, api_resource_response


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tests', methods=[POST])
def test():
    data = request.json
    return 'Hello ' + data['nombre']


@app.route(BASE_URI_V1 + URI_PRODUCTS, methods=[POST])
def create_product_api():
    dto_product = request.json
    code, product = create_product(dto_product)
    if code is CREATED or CONFLICT:
        return api_response(product.barcode, URI_PRODUCTS, code)
    else:
        return api_error_response(code)


@app.route(BASE_URI_V1 + URI_PRODUCTS + BARCODE_PARAM, methods=[PUT, GET])
def manage_product_by_barcode_api(barcode):
    dto_product = request.json
    if request.method == PUT:
        code, product = update_product(barcode, dto_product)
        if code is OK:
            return api_response(product.barcode, URI_PRODUCTS, code)
        else:
            return api_error_response(code)
    if request.method == GET:
        code, product = get_product_by_barcode(barcode)
        if code is OK:
            return api_resource_response(product)
        else:
            return api_error_response(code)




