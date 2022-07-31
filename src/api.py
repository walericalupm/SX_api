
from src.response import api_response
from src.app import app
from flask import request
from src.constants import *
from src.queries import create_product, update_product, get_product_by_barcode, get_products
from src.utils import api_resource_response, api_error_response


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tests', methods=[POST])
def test():
    data = request.json
    return 'Hello ' + data['nombre']


@app.route(BASE_URI_V1 + URI_PRODUCTS, methods=[GET, POST])
def manage_product_api():
    if request.method == GET:
        code, product = get_products()
    else:
        dto_product = request.json
        code, product = create_product(dto_product)
    if code is OK:
        return api_resource_response(product, code)
    if code is CREATED or CONFLICT:
        return api_response(product['barcode'], URI_PRODUCTS, code)
    else:
        return api_error_response(code)


@app.route(BASE_URI_V1 + URI_PRODUCTS + BARCODE_PARAM, methods=[PUT, GET])
def manage_product_by_barcode_api(barcode):
    if request.method == PUT:
        dto_product = request.json
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




