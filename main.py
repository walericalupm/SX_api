from src.models import *
from src.views import *


def create_tables():
    with db:
        db.create_tables([Product, Purchase])


if __name__ == '__main__':
    create_tables()
    app.debug = True
    app.run(debug=True)
