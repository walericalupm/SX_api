import unittest
from faker import Faker
from random import seed, randint
from src.configuration import TestingConfig
import src.models as models


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_database()
        recreate_database()


    @classmethod
    def tearDownClass(cls):
        drop_tables()
        destroy_database()


products_generated = list()
purchases_generated = list()


def load_database():
    models.remote_db.initialize(TestingConfig.DATABASE)


def recreate_database():
    drop_tables()
    clean_data()
    create_tables()
    seed_database()


def create_tables():
    models.remote_db.create_tables([models.Product, models.Purchase])


def drop_tables():
    models.remote_db.drop_tables([models.Product, models.Purchase])


def clean_data():
    products_generated.clear()
    purchases_generated.clear()


def seed_database(num_registers=10):
    # region Product
    for _ in range(num_registers):
        product_to_save = generate_random_product()
        products_generated.append(product_to_save)
        product_to_save.save()
    # endregion
    # region Purchases
    for _ in range(num_registers * 2):
        seed(1)
        product_position = randint(0, num_registers)
        purchase_to_save = generate_random_purchase(products_generated[product_position])
        purchases_generated.append(purchase_to_save)
        purchase_to_save.save()
    # endregion


def destroy_database():
    models.remote_db.close()


def generate_random_product():
    fake = Faker()
    seed(0)
    return models.Product(code=fake.bothify(text='TE_###_###'),
                          barcode=fake.ean(length=8),
                          name=fake.bothify(text='T_Product_##'),
                          category=fake.bothify(text='TEST_#'),
                          supermarket=fake.bothify(text='Supermarket_##'),
                          price=fake.pyfloat(left_digits=2, right_digits=2, positive=True))


def generate_random_purchase(product):
    seed(1)
    return models.Purchase(product=product, quantity=randint(0, 10), purchase_price=product.price)
