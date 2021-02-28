from playhouse.shortcuts import model_to_dict
from tests.base_test_setup import BaseTestCase, generate_random_product
from src.views import *
import src.models as models
from app import app


class ITAPIProduct(BaseTestCase):

    def setUp(self):
        models.remote_db.close()

    def test_create_product(self):
        with app.test_client() as client:
            # Given
            product_to_create = model_to_dict(generate_random_product())
            # When
            create_url = BASE_URI_V1 + URI_PRODUCTS
            headers = {'Content-Type': 'application/json'}
            response = client.post(create_url, json=product_to_create)

            # Then
            self.assertEqual(CREATED, response.status_code)
