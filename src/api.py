from src.response import api_response
from src.app import app
from flask import request
from src.constants import *
from src.queries import create_product, update_product, get_product_by_barcode, get_products, create_purchase
from src.utils import api_resource_response, api_error_response


@app.route('/')
def hello_world():
    return 'SX_api running!'


@app.route(BASE_URI_V1 + URI_PRODUCT, methods=[GET, POST])
def manage_product_api():
    if request.method == GET:
        code, product = get_products()
    else:
        dto_product = request.json
        code, product = create_product(dto_product)
    if code is OK:
        return api_resource_response(product, code)
    if code is CREATED or code is CONFLICT:
        return api_response(product['barcode'], URI_PRODUCT, code)
    else:
        return api_error_response(code)


@app.route(BASE_URI_V1 + URI_PRODUCT + BARCODE_PARAM, methods=[PUT, GET])
def manage_product_by_barcode_api(barcode):
    if request.method == PUT:
        dto_product = request.json
        code, product = update_product(barcode, dto_product)
        if code is OK:
            return api_response(product.barcode, URI_PRODUCT, code)
        else:
            return api_error_response(code)
    if request.method == GET:
        code, product = get_product_by_barcode(barcode)
        if code is OK:
            return api_resource_response(product)
        else:
            return api_error_response(code)


@app.route(BASE_URI_V1 + URI_PURCHASE, methods=[POST])
def create_purchase_api():
    dto_purchase = request.json
    code, query_response = create_purchase(dto_purchase)
    if code is CREATED:
        purchase = query_response
        return api_response(str(purchase['id']), URI_PURCHASE, code)
    else:
        error_message = query_response
        return api_error_response(code, error_message)





