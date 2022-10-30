import datetime
from peewee import Model, CharField, ForeignKeyField, IntegerField, FloatField, DateTimeField, MySQLDatabase, \
    DatabaseProxy

remote_db = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = remote_db


class Product(BaseModel):
    code = CharField(max_length=10, null=True)
    barcode = CharField(max_length=50, unique=True)
    name = CharField(max_length=50)
    category = CharField(max_length=50, null=True)
    supermarket = CharField(max_length=70)
    price = FloatField(null=True, default=0.0)
    quantity = IntegerField(null=True, default=1)


class Purchase(BaseModel):
    product = ForeignKeyField(Product, backref='purchase')
    quantity = IntegerField()
    purchase_price = FloatField()
    date = DateTimeField(default=datetime.datetime.now)
