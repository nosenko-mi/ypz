import pytest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import uuid


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/customer/account/create/')
    yield browser
    browser.quit()


class TestRegister():

    def fill_info(self, browser):
        try:
            browser.find_element(
                By.ID, 'firstname').send_keys(self.first_name)
            browser.find_element(
                By.ID, 'lastname').send_keys(self.last_name)
            browser.find_element(
                By.ID, 'email_address').send_keys(self.email)
            browser.find_element(
                By.ID, 'password').send_keys(self.password)
            browser.find_element(
                By.ID, 'confirmation').send_keys(self.password)
            browser.find_element(
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

    @pytest.mark.smoke
    @pytest.mark.slow
    def test_registered_user_should_be_redirected_to_my_account_page(self, browser):
        self.get_info()
        self.fill_info(browser)

        dashboard = None
        try:
            dashboard = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'customer-account-index.customer-account-totals'))
            )
        except TimeoutException as e:
            print(e)

        assert dashboard is not None, 'User should be redirected to "My account" page'

    @pytest.mark.smoke
    def test_error_is_shown_if_user_already_exists(self, browser):
        self.first_name = 'user'
        self.last_name = 'exists'
        self.email = 'userexists111@gmail.com'
        self.password = 'userexists111'

        self.fill_info(browser)

        error = WebDriverWait(browser, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-msg')))

        assert error is not None, 'Error message shoud pop up if user already exists.'
