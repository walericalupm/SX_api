from playhouse.shortcuts import model_to_dict
from tests.base_test_setup import BaseTestCase, generate_random_product, products_generated
from src.api import *
import src.models as models
from src.app import app


class ITAPIProduct(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

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
            products_url = BASE_URI_V1 + URI_PRODUCTS
            response = client.get(products_url)
            products = response.data

            products_generated_number = len(products_generated)

            # self.assertEqual(, len(products))


