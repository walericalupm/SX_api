from peewee import IntegrityError

from testing_suite.base_test_case import BaseTestCase
from src.models import Product


class ITDBProduct(BaseTestCase):

    def test_create_product(self):
        products_number = len(Product.select())
        product_to_create = Product(code='TE_001_001', barcode='1001', name='T_Product_1', category='TEST_1',
                                    supermarket='Test', price=9.99)
        product_to_create.save()
        new_products_number = len(Product.select())
        products_number = products_number + 1
        product_created = Product.select().where(Product.barcode == '1001').get()

        self.assertEqual(new_products_number, products_number)
        self.assertEqual(product_created.code, product_to_create.code)
        self.assertEqual(product_created.barcode, product_to_create.barcode)
        self.assertEqual(product_created.name, product_to_create.name)
        self.assertEqual(product_created.category, product_to_create.category)
        self.assertEqual(product_created.supermarket, product_to_create.supermarket)
        self.assertEqual(product_created.price, product_to_create.price)
        product_created.delete_instance()

    def test_create_duplicated_product(self):
        product_to_create = Product(code='TE_001_001', barcode='0000000001', name='T_Product_1', category='TEST_1',
                                    supermarket='Test', price=9.99)
        self.assertRaises(IntegrityError, product_to_create.save())

    def test_create_product2(self):
        self.assertTrue(True, True)

    def test_create_product3(self):
        self.assertTrue(True, True)
