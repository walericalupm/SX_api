import unittest
from faker import Faker
from random import seed, randint
from src.models import remote_db, Product, Purchase


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_database()
        drop_tables()
        create_tables()
        seed_database()

    @classmethod
    def tearDownClass(cls):
        drop_tables()


products_generated = []
purchases_generated = []


def init_database():
    # region database_seeder_setup
    # Database for testing
    # TODO: Set in config file
    remote_db.init('It3vTRTHBk',
                   user='It3vTRTHBk',
                   password='2tgt40lmx2',
                   host='remotemysql.com',
                   port=3306
                   )


def create_tables():
    with remote_db:
        remote_db.create_tables([Product, Purchase])


def drop_tables():
    with remote_db:
        remote_db.drop_tables([Product, Purchase])


def seed_database(num_registers=5):
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


def generate_random_product():
    fake = Faker()
    seed(0)
    return Product(code=fake.bothify(text='TE_###_###'),
                   barcode=fake.ean(length=8),
                   name=fake.bothify(text='T_Product_##'),
                   category=fake.bothify(text='TEST_#'),
                   supermarket=fake.bothify(text='Supermarket_##'),
                   price=fake.pyfloat(left_digits=2, right_digits=2, positive=True))


def generate_random_purchase(product):
    seed(1)
    return Purchase(product=product, quantity=randint(0, 10))
# endregion
