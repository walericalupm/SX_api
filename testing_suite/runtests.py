import unittest
from database_seeder import *
from testing_suite.integration_test.database.itdb_product import ITDBProduct


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(ITDBProduct('test_create_product'))
    return suite


if __name__ == '__main__':
    setUpModule()
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
    tearDownModule()
