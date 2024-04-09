import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/')
    yield browser
    browser.quit()


class TestCategory():

    @pytest.mark.smoke
    def test_sarch_denim_should_return_2_elements(self, browser):

        self.search_field = browser.find_element(By.ID, 'search')
        self.search_field.send_keys('Denim')
        self.search_field.submit()

        products = browser.find_elements(
            By.XPATH, '//span[@class="price"]')

        assert 2 == len(products), 'Number of denim product shoul be 2.'


