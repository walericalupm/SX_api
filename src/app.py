from flask import Flask
import src.models as models
from dotenv import dotenv_values

app = Flask(__name__)


def create_tables():
    with models.remote_db as db:
        db.create_tables([models.Product, models.Purchase])


def load_database(database):
    models.remote_db.initialize(database)
    create_tables()


@app.before_request
def before_request():
    if models.remote_db.is_closed():
        models.remote_db.connect()


@app.after_request
def after_request(response):
    models.remote_db.close()
    return response
