import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


test_data = [
    ("userexists111@gmail.com", "userexists111", "customer-account-index.customer-account", "Existing user should be redirected to 'My account' page"),
    ("userdoesnotexist121@gmail.com", "userexists121", "error-msg", "Error message shoud pop up if user does not exist."),
    ("userexists111@gmail.com", "userexists222", "error-msg", "Error message shoud pop up if user does not exist."),
]



@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/customer/account/login/')
    yield browser
    browser.quit()


class TestLogin():

    def fill_info(self, browser, email, password):
        try:
            browser.find_element(By.ID, 'email').send_keys(email)
            browser.find_element(By.ID, 'pass').send_keys(password)
            browser.find_element(By.ID, 'send2').submit()
            return 1
        except Exception as e:
            print(e)
            return -1
        

    @pytest.mark.parametrize("email, password, expected_element_class_name, error_message", test_data)
    def test_login_with_data(self, browser, email, password, expected_element_class_name, error_message):

        self.fill_info(browser, email, password)

        real = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, expected_element_class_name)))

        assert real is not None, error_message


    # @pytest.mark.smoke
    # @pytest.mark.slow
    # def test_user_log_in_successfully(self, browser):
    #     self.email = 'userexists111@gmail.com'
    #     self.password = 'userexists111'

    #     self.fill_info(browser)

    #     dashboard = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located(
    #             (By.CLASS_NAME, 'customer-account-index.customer-account'))
    #     )

    #     assert dashboard is not None, 'User should be redirected to "My account" page'

    # @pytest.mark.smoke
    # def test_error_is_shown_if_log_in_failed(self, browser):
    #     self.email = 'userexists121@gmail.com'
    #     self.password = 'userexists121'

    #     self.fill_info(browser)

    #     error = WebDriverWait(browser, 2).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, 'error-msg')))

    #     assert error is not None, 'Error message shoud pop up if user does not exist.'
