from src.views import *
from app import app, load_database


if __name__ == '__main__':
    load_database()
    app.debug = True
    app.run(debug=True)
