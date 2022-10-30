import json

from playhouse.shortcuts import model_to_dict
from tests.base_test_setup import BaseTestCase, generate_random_product, products_generated, recreate_database
from src.api import create_product
from src.constants import BASE_URI_V1, URI_PRODUCTS, CREATED
from src.app import app


class ITAPIProduct(BaseTestCase):

    def setUp(self):
        recreate_database()

    def test_create_product(self):
        with app.test_client() as client:
            # Given
            product_to_create = model_to_dict(generate_random_product())
            # When
            create_url = BASE_URI_V1 + URI_PRODUCTS
            response = client.post(create_url, json=product_to_create)

            # Then
            self.assertEqual(CREATED, response.status_code)

    def test_get_all_products(self):
        with app.test_client() as client:
            # Given
            number_products_generated = len(products_generated)
            # When
            products_url = BASE_URI_V1 + URI_PRODUCTS
            response = client.get(products_url)
            products_from_api = json.loads(response.data)
            number_products_from_api = len(products_from_api)

            # Then
            self.assertEqual(number_products_generated, number_products_from_api)


