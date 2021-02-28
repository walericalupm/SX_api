from faker import Faker
from peewee import IntegrityError, DoesNotExist
from tests.base_test_setup import BaseTestCase, generate_random_product, products_generated
import src.models as models


class ITDBProduct(BaseTestCase):

    def test_create_product(self):
        products_number = len(models.Product.select())
        product_to_create = generate_random_product()
        product_to_create.save()
        new_products_number = len(models.Product.select())
        product_created = models.Product.select().where(models.Product.barcode == product_to_create.barcode).get()

        self.assertEqual(new_products_number, products_number + 1)
        self.assertEqual(product_created.code, product_to_create.code)
        self.assertEqual(product_created.barcode, product_to_create.barcode)
        self.assertEqual(product_created.name, product_to_create.name)
        self.assertEqual(product_created.category, product_to_create.category)
        self.assertEqual(product_created.supermarket, product_to_create.supermarket)
        self.assertEqual(product_created.price, product_to_create.price)
        product_created.delete_instance()

    def test_create_duplicated_product(self):
        product_to_create = generate_random_product()
        product_to_create.barcode = products_generated[0].barcode
        self.assertRaises(IntegrityError, product_to_create.save)

    def test_get_product(self):
        existing_product = products_generated[0]
        self.assertIsNotNone(existing_product)

    def test_get_non_existent_product(self):
        fake = Faker()
        Faker.seed(0)
        empty_product = models.Product.select().where(models.Product.barcode == fake.ean(length=8))
        self.assertRaises(DoesNotExist, empty_product.get)

    def test_update_product(self):
        new_price = 10.00
        new_category = 'CAT4'
        product_barcode = products_generated[0].barcode

        product_to_update = models.Product.select().where(models.Product.barcode == product_barcode).get()
        product_to_update.price = new_price
        product_to_update.category = new_category
        product_to_update.save()

        product_updated = models.Product.select().where(models.Product.barcode == product_barcode).get()
        self.assertEqual(product_updated.price, new_price)
        self.assertEqual(product_updated.category, new_category)

    def test_delete_product(self):
        product = generate_random_product()
        product.save()
        delete_query = models.Product.delete().where(models.Product.barcode == product.barcode)
        delete_query.execute()
        product_deleted = models.Product.select().where(models.Product.barcode == product.barcode)
        self.assertRaises(DoesNotExist, product_deleted.get)


