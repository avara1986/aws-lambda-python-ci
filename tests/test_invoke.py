# coding=utf-8
# python imports
from __future__ import unicode_literals, print_function, absolute_import

import os
import unittest

from myexamplelambdaproject.lambda1.main import my_handler as mh1
from myexamplelambdaproject.lambda2.main import my_handler as mh2

TESTS_PATH = os.path.dirname(os.path.abspath(__file__))

class InvokeTest(unittest.TestCase):
    EXAMPLE_PROJECT = "myexamplelambdaproject"

    def setUp(self):
        pass

    def test_func1(self):
        result = mh1({}, {})
        self.assertTrue(result['message'] == 'Hello world lambda1!')

        result = mh2({}, {})
        self.assertTrue(result['message'] == 'Hello world lambda2!')


if __name__ == '__main__':
    unittest.main()
