from flask import flash
from peewee import IntegrityError
from models import *
from app import db
from constants import *


def create_product(dto_product):
    try:
        with db.atomic():
            product = Product.create(
                code=dto_product['code'],  # Generate Code
                barcode=dto_product['barcode'],
                name=dto_product['name'],
                category=dto_product['category'],
                supermarket=dto_product['supermarket']
            )
            return CREATED, product
    except IntegrityError:
        product = get_product_by_barcode(dto_product['barcode'])
        return CONFLICT, product
    except:
        return SERVER_ERROR, None


def update_product(barcode, dto_product):
    product = get_product_by_barcode(barcode)
    if 'quantity' in dto_product.keys():
        product.quantity = product.quantity + int(dto_product['quantity'])
        product.save()
        return OK, product
    else:
        # TODO: Implement complete update
        return SERVER_ERROR, None


def get_product_by_barcode(barcode):
    return (Product
            .select()
            .where(Product.barcode == barcode).get())

#
#
# def get_art_paintings_by_code(code):
#     return (Paint
#             .select()
#             .where(Paint.Code == code).get())
