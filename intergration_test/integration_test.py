# -*- coding: utf-8 -*-
"""
    integration_test

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

if __name__ == "__main__":
    selenium_tests = unittest.TestLoader().discover('integration_test', pattern='*.py')

    unittest.TextTestRunner().run(selenium_tests)
