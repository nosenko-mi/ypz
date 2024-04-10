import pytest

from base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    _email_field_locator = (By.ID, 'email')
    _password_field_locator = (By.ID, 'pass')
    _login_button_locator = (By.ID, 'send2')

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # def _validate_page(self, email, password, expected_element_class_name, error_message):
    #     self.fill_field(self.driver, self._email_field_locator, email)
    #     self.fill_field(self.driver, self._password_field_locator, password)
    #     self.click_button(self.driver, self._login_button_locator)

    #     real = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.CLASS_NAME, expected_element_class_name)))
    #     assert real is not None, error_message

    def login_with_data(self, data):
        # self.fill_info(browser, data['email'], data['password'])
        self.fill_field(self._email_field_locator, data['email'])
        self.fill_field(self._password_field_locator, data['password'])
        self.click_button(self._login_button_locator)
        try:
            real = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, data['element'])))
            return real
        except Exception as e:
            print(e)
            return None
