from src.api import *
from src.app import app, load_database


if __name__ == '__main__':
    load_database()
    app.debug = True
    app.run(debug=True)
