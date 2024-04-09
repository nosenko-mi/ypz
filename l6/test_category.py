import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCategory(unittest.TestCase):

    def setUp(self) -> None:

        self.driver = webdriver.Firefox()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_sarch_denim_should_return_2_elements(self):

        self.search_field = self.driver.find_element(By.ID, 'search')
        self.search_field.send_keys('Denim')
        self.search_field.submit()

        products = self.driver.find_elements(
            By.XPATH, '//span[@class="price"]')

        self.assertEqual(2, len(products),
                         'Number of denim product shoul be 2')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__name__':
    unittest.main()
