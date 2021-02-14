import unittest
from src.models import remote_db
from testing_suite.database_seeder import DATABASE_NAME, \
    DATABASE_PORT, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_USERNAME


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        remote_db.init(DATABASE_NAME,
                       user=DATABASE_USERNAME,
                       password=DATABASE_PASSWORD,
                       host=DATABASE_HOST,
                       port=DATABASE_PORT
                       )


