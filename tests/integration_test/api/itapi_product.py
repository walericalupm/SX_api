from playhouse.shortcuts import model_to_dict

from tests.base_test_setup import BaseTestCase, generate_random_product, init_database
from src.views import *
from src.app import remote_db


class ITAPIProduct(BaseTestCase):
    # client = None

    def test_create_product(self):
        with app.test_client() as client:
            init_database()
            # Given
            product_to_create = model_to_dict(generate_random_product())
            # When
            create_url = BASE_URI_V1 + URI_PRODUCTS
            # headers = {'Content-Type': 'application/json'}
            response = client.get('/')

            # Then
            self.assertEqual(CREATED, response.status_code)
