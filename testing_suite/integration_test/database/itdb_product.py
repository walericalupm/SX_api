from peewee import IntegrityError, DoesNotExist
from testing_suite.base_test_setup import BaseTestCase
from src.models import Product
from faker import Faker


class ITDBProduct(BaseTestCase):

    def generate_random_product(self):
        fake = Faker()
        Faker.seed(0)
        return Product(code = fake.bothify(text='TE_###_###'),
                       barcode = fake.ean(length=8),
                       name=fake.bothify(text='T_Product_##'),
                       category=fake.bothify(text='TEST_#'),
                       supermarket=fake.bothify(text='Supermarket_##'),
                       price=fake.pyfloat(left_digits=2,right_digits=2, positive=True))


    def test_create_product(self):
        products_number = len(Product.select())
        product_to_create = Product(code='TE_001_001', barcode='1001', name='T_Product_1', category='TEST_1',
                                    supermarket='Test', price=9.99)
        product_to_create.save()
        new_products_number = len(Product.select())
        product_created = Product.select().where(Product.barcode == '1001').get()

        self.assertEqual(new_products_number, products_number + 1)
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
        self.assertRaises(IntegrityError, product_to_create.save)

    def test_get_product(self):
        existing_product = Product.select().where(Product.barcode == '0000000002').get()
        self.assertIsNotNone(existing_product)

    def test_get_non_existent_product(self):
        empty_product = Product.select().where(Product.barcode == '1111111111')
        self.assertRaises(DoesNotExist, empty_product.get)

    def test_update_product(self):
        new_price = 10.00
        new_category = 'CAT4'
        product_barcode = '0000000011'

        product_to_update = Product.select().where(Product.barcode == product_barcode).get()
        product_to_update.price = new_price
        product_to_update.category = new_category
        product_to_update.save()

        product_updated = Product.select().where(Product.barcode == product_barcode).get()
        self.assertEqual(product_updated.price, new_price)
        self.assertEqual(product_updated.category, new_category)

    def test_delete_product(self):
        product = self.generate_random_product()
        product.save()
        delete_query = Product.delete().where(Product.barcode == product.barcode)
        delete_query.execute()
        product_deleted = Product.select().where(Product.barcode == product.barcode)
        self.assertRaises(DoesNotExist, product_deleted.get)


