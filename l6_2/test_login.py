import pytest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/customer/account/login/')
    yield browser
    browser.quit()


class TestLogin():

    def fill_info(self, browser):
        try:
            browser.find_element(By.ID, 'email').send_keys(self.email)
            browser.find_element(By.ID, 'pass').send_keys(self.password)
            browser.find_element(By.ID, 'send2').submit()
            return 1
        except Exception as e:
            print(e)
            return -1

    @pytest.mark.smoke
    @pytest.mark.slow
    def test_user_log_in_successfully(self, browser):
        self.email = 'userexists111@gmail.com'
        self.password = 'userexists111'

        self.fill_info(browser)

        dashboard = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'customer-account-index.customer-account'))
        )

        assert dashboard is not None, 'User should be redirected to "My account" page'

    @pytest.mark.smoke
    def test_error_is_shown_if_log_in_failed(self, browser):
        self.email = 'userexists121@gmail.com'
        self.password = 'userexists121'

        self.fill_info()

        error = WebDriverWait(browser, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-msg')))

        assert error is not None, 'Error message shoud pop up if user does not exist.'
