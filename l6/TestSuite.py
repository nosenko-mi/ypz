import unittest
from test_cart import TestCart
from test_category import TestCategory
from test_register import TestRegister
from test_login import TestLogin


cart_tests = unittest.TestLoader().loadTestsFromTestCase(TestCart)
category_tests = unittest.TestLoader().loadTestsFromTestCase(TestCategory)
register_tests = unittest.TestLoader().loadTestsFromTestCase(TestRegister)
login_tests = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

all_tests = unittest.TestSuite([cart_tests, category_tests, register_tests, login_tests])

unittest.TextTestRunner().run(all_tests)