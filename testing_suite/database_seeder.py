from peewee import MySQLDatabase
from src.models import Product, Purchase, remote_db

# Database for testing
DATABASE_NAME = 'SQ4Y6h3Ze5'
DATABASE_USERNAME = 'SQ4Y6h3Ze5'
DATABASE_PASSWORD = '7wW8rMNehQ'
DATABASE_PORT = 3306
DATABASE_HOST = 'remotemysql.com'


remote_db.init(
    DATABASE_NAME,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)
db = remote_db


def create_tables():
    with db:
        db.create_tables([Product, Purchase])


def drop_tables():
    with db:
        db.drop_tables([Product, Purchase])


def seed_database():
    # region Product
    product_1_barcode, \
    product_2_barcode, \
    product_3_barcode, \
    product_4_barcode, \
    product_5_barcode = \
        '0000000001', \
        '0000000002', \
        '0000000011', \
        '0000000111', \
        '1000000001'
    product = Product(code='ME_001_001', barcode=product_1_barcode, name='M_Product_1', category='CAT1',
                      supermarket='Mercadona', price=5.99)
    product.save()
    product = Product(code='ME_001_002', barcode=product_2_barcode, name='M_Product_2', category='CAT1',
                      supermarket='Mercadona', price=6.99)
    product.save()
    product = Product(code='HC_001_001', barcode=product_3_barcode, name='H_Product_1', category='CAT2',
                      supermarket='Hipercor', price=2.00)
    product.save()
    product = Product(code='CA_001_001', barcode=product_4_barcode, name='C_Product_1', category='CAT1',
                      supermarket='Carrefour', price=4.99)
    product.save()
    product = Product(code='LI_001_001', barcode=product_5_barcode, name='L_Product_1', category='CAT4',
                      supermarket='LIDL', price=10.50)
    product.save()
    # endregion
    # region Purchases
    product_1 = Product.select().where(Product.barcode == product_1_barcode).get()
    product_2 = Product.select().where(Product.barcode == product_2_barcode).get()
    product_3 = Product.select().where(Product.barcode == product_3_barcode).get()
    product_4 = Product.select().where(Product.barcode == product_4_barcode).get()
    product_5 = Product.select().where(Product.barcode == product_5_barcode).get()

    purchase = Purchase(product=product_1, quantity=3)
    purchase.save()
    purchase = Purchase(product=product_2, quantity=1)
    purchase.save()
    purchase = Purchase(product=product_2, quantity=3)
    purchase.save()
    purchase = Purchase(product=product_4, quantity=5)
    purchase.save()
    purchase = Purchase(product=product_3, quantity=1)
    purchase.save()
    purchase = Purchase(product=product_3, quantity=10)
    purchase.save()
    # endregion


def setUpModule():
    create_tables()
    seed_database()


def tearDownModule():
    drop_tables()
