from flask import Flask
import src.models as models
from dotenv import dotenv_values

app = Flask(__name__)


def create_tables():
    with models.remote_db as db:
        db.create_tables([models.Product, models.Purchase])


def load_database():
    db_params = dotenv_values()
    models.remote_db.init(
        db_params.get('DATABASE_NAME'),
        user=db_params.get('DATABASE_USERNAME'),
        password=db_params.get('DATABASE_PASSWORD'),
        host=db_params.get('DATABASE_HOST'),
        port=int(db_params.get('DATABASE_PORT'))
    )
    create_tables()


@app.before_request
def before_request():
    print("========> Hey!")
    models.remote_db.connect()


@app.after_request
def after_request(response):
    models.remote_db.close()
    return response
