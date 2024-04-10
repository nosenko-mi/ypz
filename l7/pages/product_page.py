import pytest

from base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def add_product_to_cart_with_qty(self, qty):
        self.color_box = self.driver.find_element(By.ID, 'option22')
        self.color_box.click()

        self.size_box = self.driver.find_element(By.ID, 'option78')
        self.size_box.click()

        self.qty_field = self.driver.find_element(By.ID, 'qty')
        self.qty_field.clear()
        self.qty_field.send_keys(qty)

        self.add_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#product_addtocart_form > div.product-shop > div.product-options-bottom > div.add-to-cart > div.add-to-cart-buttons > button'))
        )

        self.add_button.click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'cart-totals')))

            cart_qty = self.driver.find_element(
                By.CLASS_NAME, 'input-text.qty').get_attribute('value')

            return int(cart_qty)
        except Exception as e:
            print(e)
            return None
