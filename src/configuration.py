from dotenv import dotenv_values
from peewee import DatabaseProxy, MySQLDatabase, SqliteDatabase, PostgresqlDatabase


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DATABASE = DatabaseProxy()
    LOG_FILE = 'SX_api.log'


class ProductionConfig(Config):

    @property
    def DATABASE(self):
        db_params = dotenv_values()
        return MySQLDatabase(
            db_params.get('DATABASE_NAME'),
            user=db_params.get('DATABASE_USERNAME'),
            password=db_params.get('DATABASE_PASSWORD'),
            host=db_params.get('DATABASE_HOST'),
            port=int(db_params.get('DATABASE_PORT'))
        )


class CloudConfig(Config):
    @property
    def DATABASE(self):
        db_params = dotenv_values('.cloud.env')
        return PostgresqlDatabase(
            db_params.get('DATABASE_NAME'),
            user=db_params.get('DATABASE_USERNAME'),
            password=db_params.get('DATABASE_PASSWORD'),
            host=db_params.get('DATABASE_HOST'),
            port=int(db_params.get('DATABASE_PORT'))
        )


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    DATABASE = SqliteDatabase('sx.db')
    LOG_FILE = "development.SX_api.log"


class TestingConfig(Config):
    DEBUG = True
    DATABASE = SqliteDatabase(':memory:')
    LOG_FILE = "testing.SX_api.log"
