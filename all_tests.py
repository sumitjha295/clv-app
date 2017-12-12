import unittest
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/src/includes')
sys.path.insert(0, current_path + '/tests')

from test_db_controller import TestDbController
from test_clv_utils import TestCLVUtils


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestDbController())
    test_suite.addTest(TestCLVUtils())
    return test_suite


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
