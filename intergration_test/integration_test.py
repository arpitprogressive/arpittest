import unittest

if __name__ == "__main__":
    selenium_tests = unittest.TestLoader().discover('integration_test', pattern='*.py')

    unittest.TextTestRunner().run(selenium_tests)
