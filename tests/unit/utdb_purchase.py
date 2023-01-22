from src.constants import CREATED, OK, NOT_FOUND, UNPROCESSABLE_ENTITY, PRODUCT_BARCODE_NOT_EXIST
from src.dto import PurchaseDto
from tests.base_setup import BaseTestCase, products_generated, generate_random_purchase, generate_random_product
from unittest.mock import MagicMock
from playhouse.shortcuts import model_to_dict
import src.models as models
import src.queries as queries


class UTDBPurchase(BaseTestCase):

    def test_create_purchase(self):
        # Given
        queries_mock = MagicMock()
        queries_mock.get_product_by_barcode.return_value = OK, model_to_dict(products_generated[0])
        queries.get_product_by_barcode = queries_mock.get_product_by_barcode

        purchase_mock = MagicMock()
        purchase_mock.save.return_value = True
        models.Purchase.save = purchase_mock.save

        purchase_to_create = generate_random_purchase(products_generated[0])
        purchase_to_create_dict = model_to_dict(purchase_to_create)
        purchase_dto = PurchaseDto(**purchase_to_create_dict)
        purchase_dto.product_barcode = products_generated[0].barcode

        # When
        code, purchase_created = queries.create_purchase(purchase_dto.dict())

        # Then
        self.assertEqual(code, CREATED)
        self.assertEqual(purchase_created['quantity'], purchase_to_create_dict['quantity'])
        self.assertEqual(purchase_created['purchase_price'], purchase_to_create_dict['purchase_price'])
        self.assertEqual(purchase_created['product']['barcode'], purchase_to_create_dict['product']['barcode'])

    def test_create_purchase_product_barcode_non_existent(self):
        # Given
        queries_mock = MagicMock()
        queries_mock.get_product_by_barcode.return_value = NOT_FOUND, None
        queries.get_product_by_barcode = queries_mock.get_product_by_barcode

        random_product = generate_random_product()
        purchase_to_create = generate_random_purchase(random_product)
        purchase_to_create_dict = model_to_dict(purchase_to_create)
        purchase_dto = PurchaseDto(**purchase_to_create_dict)
        purchase_dto.product_barcode = random_product.barcode

        # When
        code, response_message = queries.create_purchase(purchase_dto.dict())

        # Then
        self.assertEqual(code, UNPROCESSABLE_ENTITY)
        self.assertEqual(response_message, PRODUCT_BARCODE_NOT_EXIST)
