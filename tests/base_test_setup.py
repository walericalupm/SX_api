import unittest
from faker import Faker
from dotenv import dotenv_values
from random import seed, randint
from src.constants import ENV_TEST_DIR
import src.models as models


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_database()
        drop_tables()
        create_tables()
        seed_database()

    @classmethod
    def tearDownClass(cls):
        drop_tables()


products_generated = []
purchases_generated = []


def load_database():
    db_params = dotenv_values(ENV_TEST_DIR)
    models.remote_db.init(
        db_params.get('DATABASE_NAME'),
        user=db_params.get('DATABASE_USERNAME'),
        password=db_params.get('DATABASE_PASSWORD'),
        host=db_params.get('DATABASE_HOST'),
        port=int(db_params.get('DATABASE_PORT'))
    )


def create_tables():
    with models.remote_db as db:
        db.create_tables([models.Product, models.Purchase])


def drop_tables():
    with models.remote_db as db:
        db.drop_tables([models.Product, models.Purchase])


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
    return models.Product(code=fake.bothify(text='TE_###_###'),
                          barcode=fake.ean(length=8),
                          name=fake.bothify(text='T_Product_##'),
                          category=fake.bothify(text='TEST_#'),
                          supermarket=fake.bothify(text='Supermarket_##'),
                          price=fake.pyfloat(left_digits=2, right_digits=2, positive=True))


def generate_random_purchase(product):
    seed(1)
    return models.Purchase(product=product, quantity=randint(0, 10))
# endregion
