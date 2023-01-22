from src.constants import URI_PURCHASE, BASE_URI_V1, CREATED
from tests.base_setup import BaseTestCase, recreate_database, products_generated, generate_random_purchase
from playhouse.shortcuts import model_to_dict
from src.api import create_purchase
from src.app import app
from src.dto import PurchaseDto


class ITAPIPurchase(BaseTestCase):
    def setUp(self):
        recreate_database()

    def test_create_purchase(self):
        with app.test_client() as client:
            # Given
            product_purchased = products_generated[0]
            purchase_to_create = generate_random_purchase(product_purchased)
            purchase_to_create_dict = model_to_dict(purchase_to_create)
            purchase_dto = PurchaseDto(**purchase_to_create_dict)
            purchase_dto.product_barcode = product_purchased.barcode

            # When
            create_url = BASE_URI_V1 + URI_PURCHASE
            response = client.post(create_url, json=purchase_dto.dict())

            # Then
            self.assertEqual(CREATED, response.status_code)

