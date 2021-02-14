from models import remote_db
from flask import Flask

DATABASE_NAME = 'fPFDbFxX0z'
DATABASE_USERNAME = 'fPFDbFxX0z'
DATABASE_PASSWORD = 'VCuV9ETNiF'
DATABASE_PORT = 3306
DATABASE_HOST = 'remotemysql.com'

remote_db.init(
    DATABASE_NAME,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)

app = Flask(__name__)


@app.before_request
def before_request():
    remote_db.connect()


@app.after_request
def after_request(response):
    remote_db.close()
    return response
