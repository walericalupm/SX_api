import logging
from peewee import IntegrityError, DoesNotExist
from playhouse.shortcuts import model_to_dict
import src.models as models
import src.dto as dto
from src.constants import *


def create_product(dto_product):
    try:
        with models.remote_db.atomic():
            product = models.Product.create(
                code=dto_product['code'],  # Generate Code
                barcode=dto_product['barcode'],
                name=dto_product['name'],
                category=dto_product['category'],
                supermarket=dto_product['supermarket']
            )
            return CREATED, model_to_dict(product)
    except IntegrityError:
        product = get_product_by_barcode(dto_product['barcode'])[1]
        return CONFLICT, product
    except Exception as ex:
        logging.exception(ex)
        return SERVER_ERROR, None


def update_product_quantity(barcode, quantity):
    code, product = get_product_by_barcode(barcode)
    if code is OK:
        product.quantity = product.quantity + int(quantity)
        product.save()
        return OK, product
    else:
        # TODO: Implement complete update
        return code, None


def update_product(dto_product: models.Product):
    code, product = get_product_by_barcode(dto_product.barcode)
    if code is OK:
        product.quantity = dto_product.quantity
        product.category = dto_product.category
        product.name = dto_product.name
        product.supermarket = dto_product.supermarket
        product.price = dto_product.price
        product.save()
        return OK, product
    else:
        return code, None


def get_product_by_barcode(barcode):
    try:
        product = models.Product.select().where(models.Product.barcode == barcode).get()
        return OK, model_to_dict(product)
    except DoesNotExist:
        return NOT_FOUND, None
    except Exception as ex:
        logging.exception(ex)
        return SERVER_ERROR, None


def get_products():
    try:
        products = list()
        for product in models.Product.select().dicts():
            products.append(product)
        return OK, products
    except Exception:
        return SERVER_ERROR, None


def create_purchase(dto_purchase):
    try:
        purchase_dto_model = dto.PurchaseDto(**dto_purchase)
        purchase = models.Purchase(**dto_purchase)
        code, product_dict = get_product_by_barcode(purchase_dto_model.product_barcode)
        if code is OK:
            purchase.product = models.Product(**product_dict)
            purchase.save()
            return CREATED, model_to_dict(purchase)
        if code is NOT_FOUND:
            return UNPROCESSABLE_ENTITY, PRODUCT_BARCODE_NOT_EXIST
    except Exception as ex:
        logging.exception(ex)
        return SERVER_ERROR, None


