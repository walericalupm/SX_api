from tests.base_setup import BaseTestCase, generate_random_purchase, products_generated
import src.models as models


class ITDBPurchase(BaseTestCase):

    def test_create_purchase(self):
        # Given
        purchases_quantity = len(models.Purchase.select())
        purchase_to_create = generate_random_purchase(products_generated[0])

        # When
        purchase_to_create.save()
        new_purchase_quantity = len(models.Purchase.select())
        purchase_created = models.Purchase.select().order_by(models.Purchase.id.desc()).get()

        # Then
        self.assertEqual(new_purchase_quantity, purchases_quantity + 1)
        self.assertEqual(purchase_created.product.barcode, purchase_to_create.product.barcode)
        self.assertEqual(purchase_created.quantity, purchase_to_create.quantity)
        self.assertEqual(purchase_created.purchase_price, purchase_to_create.purchase_price)
        self.assertEqual(purchase_created.date, purchase_to_create.date)
        purchase_created.delete_instance()
