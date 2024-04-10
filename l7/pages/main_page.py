import pytest

from base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    _search_field_locator = (By.ID, 'search')
    _price_text_locator = (By.XPATH, '//span[@class="price"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)


    def search_with_data(self, data):
        self.search(self._search_field_locator, data['category'])
        products = self.driver.find_elements(self._price_text_locator[0], self._price_text_locator[1])
        return len(products)



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
