import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get(
            'http://demo-store.seleniumacademy.com/elizabeth-knit-top-593.html')

    def test_multiple_items_are_added_to_cart(self):
        self.color_box = self.driver.find_element(By.ID, 'option22')
        self.color_box.click()

        self.size_box = self.driver.find_element(By.ID, 'option78')
        self.size_box.click()

        self.qty_field = self.driver.find_element(By.ID, 'qty')
        self.qty_field.clear()
        self.qty_field.send_keys(2)

        self.add_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#product_addtocart_form > div.product-shop > div.product-options-bottom > div.add-to-cart > div.add-to-cart-buttons > button'))
        )

        self.add_button.click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart-totals'))
        )

        cart_qty = self.driver.find_element(
            By.CLASS_NAME, 'input-text.qty').get_attribute('value')
        self.assertEqual(2, int(cart_qty),
                         'Number of items in cart shoul be 2')

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__name__':
    unittest.main()
