import datetime

from peewee import Model, CharField, AutoField, ForeignKeyField, IntegerField, FloatField, DateTimeField
from app import db


class BaseModel(Model):
    class Meta:
        database = db


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
    date = DateTimeField(default=datetime.datetime.now)
