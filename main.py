from src.models import *
from src.views import *
from src.app import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT


def config_database():
    with remote_db:
        remote_db.create_tables([Product, Purchase])


if __name__ == '__main__':
    config_database()
    app.debug = True
    app.run(debug=True)
