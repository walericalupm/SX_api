import logging

from src.api import *
from src.app import app, load_database
from src.configuration import ProductionConfig, DevelopmentConfig, CloudConfig

if __name__ == '__main__':
    runtime = os.getenv('RUNTIME')
    configuration = ProductionConfig() if (runtime == 'production') else DevelopmentConfig()

    if runtime == 'production':
        configuration = ProductionConfig()
    if runtime == 'cloud':
        configuration = CloudConfig()

    load_database(configuration.DATABASE)
    # logging.basicConfig(filename=configuration.LOG_FILE)

    app.config.from_object(configuration)
    app.run(port=int(os.environ.get(PORT, DEFAULT_APP_PORT)),
            debug=False,
            host=DEFAULT_APP_HOST)
