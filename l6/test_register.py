import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import uuid


class TestRegister(unittest.TestCase):

    def fill_info(self):
        try:
            self.driver.find_element(
                By.ID, 'firstname').send_keys(self.first_name)
            self.driver.find_element(
                By.ID, 'lastname').send_keys(self.last_name)
            self.driver.find_element(
                By.ID, 'email_address').send_keys(self.email)
            self.driver.find_element(
                By.ID, 'password').send_keys(self.password)
            self.driver.find_element(
                By.ID, 'confirmation').send_keys(self.password)
            self.driver.find_element(
                By.CSS_SELECTOR, '#form-validate > div.buttons-set > button').click()
            return 1
        except Exception as e:
            print(e)
            return -1

    def get_info(self):
        self.first_name = 'automated'
        self.last_name = 'test'
        id = uuid.uuid4()
        self.email = f'{self.first_name}{self.last_name}{id}@gmail.com'
        self.password = f'{self.first_name}{self.last_name}{id}'

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get(
            'http://demo-store.seleniumacademy.com/customer/account/create/')

    def test_registered_user_should_be_redirected_to_my_account_page(self):
        self.get_info()
        self.fill_info()

        dashboard = None
        try:
            dashboard = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'customer-account-index.customer-account-totals'))
            )
        except TimeoutException as e:
            print(e)

        self.assertIsNotNone(
            dashboard, 'User should be redirected to "My account" page')

    def test_error_is_shown_if_user_already_exists(self):
        self.first_name = 'user'
        self.last_name = 'exists'
        self.email = 'userexists111@gmail.com'
        self.password = 'userexists111'

        self.fill_info()

        error = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-msg')))

        self.assertIsNotNone(
            error, 'Error message shoud pop up if user already exists.')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__name__':
    unittest.main()
