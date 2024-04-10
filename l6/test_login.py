import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):

    def fill_info(self):
        try:
            self.driver.find_element(By.ID, 'email').send_keys(self.email)
            self.driver.find_element(By.ID, 'pass').send_keys(self.password)
            self.driver.find_element(By.ID, 'send2').submit()
            return 1
        except Exception as e:
            print(e)
            return -1

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get(
            'http://demo-store.seleniumacademy.com/customer/account/login/')

    def test_user_log_in_successfully(self):
        self.email = 'userexists111@gmail.com'
        self.password = 'userexists111'

        self.fill_info()

        dashboard = WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'customer-account-index.customer-account'))
        )

        self.assertIsNotNone(
            dashboard, 'User should be redirected to "My account" page')

    def test_error_is_shown_if_log_in_failed(self):
        self.email = 'userexists121@gmail.com'
        self.password = 'userexists121'

        self.fill_info()

        error = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-msg')))

        self.assertIsNotNone(
            error, 'Error message shoud pop up if user does not exist.')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__name__':
    unittest.main()
