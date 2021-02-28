from peewee import IntegrityError, DoesNotExist
from playhouse.shortcuts import model_to_dict
import src.models as models
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
            return CREATED, product
    except IntegrityError:
        product = get_product_by_barcode(dto_product['barcode'])
        return CONFLICT, product
    except:
        return SERVER_ERROR, None


def update_product(barcode, dto_product):
    code, product = get_product_by_barcode(barcode)
    if code is OK and 'quantity' in dto_product.keys():
        product.quantity = product.quantity + int(dto_product['quantity'])
        product.save()
        return OK, product
    else:
        # TODO: Implement complete update
        return code, None


def get_product_by_barcode(barcode):
    try:
        product = models.Product.select().where(models.Product.barcode == barcode).get()
        return OK, model_to_dict(product)
    except DoesNotExist:
        return NOT_FOUND, None
    except:
        return SERVER_ERROR, None
