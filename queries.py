from flask import flash
from peewee import IntegrityError

from models import *
from app import db


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
            return True
    except IntegrityError:
        flash('Barcode exists')

#
#
# def get_art_paintings_by_code(code):
#     return (Paint
#             .select()
#             .where(Paint.Code == code).get())
