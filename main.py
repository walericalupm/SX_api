import logging

from src.api import *
from src.app import app, load_database
from src.configuration import ProductionConfig, DevelopmentConfig

if __name__ == '__main__':
    runtime = os.getenv('RUNTIME')
    configuration = ProductionConfig() if (runtime == 'production') else DevelopmentConfig()

    load_database(configuration.DATABASE)
    logging.basicConfig(filename=configuration.LOG_FILE)

    app.config.from_object(configuration)
    app.run()
