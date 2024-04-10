import sys
import pytest

from selenium import webdriver

sys.path.append("D:/Programming/znu/ypz/l7/pages")
from product_page import ProductPage


test_data = [
    {"qty": 1, "expected": 1, "message": "1 item expeted in cart when 1 product added"},
    {"qty": 2, "expected": 2, "message": "2 item expeted in cart when 2 product added"},
    {"qty": 0, "expected": 1,
        "message": "1 item expeted in cart when user enters 0 as quantity"},
    {"qty": -1, "expected": 1,
     "message": "1 item expeted in cart when user enters negative value as quantity"},
    {"qty": "text", "expected": 1,
        "message": "1 item expeted in cart when user enters text as quantity"},
]


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/elizabeth-knit-top-593.html')
    yield browser
    browser.quit()


@pytest.mark.smoke
@pytest.mark.parametrize("data", test_data)
def test_multiple_items_are_added_to_cart(browser, data):

    knit_top_page = ProductPage(browser)

    cart_qty = knit_top_page.add_product_to_cart_with_qty(data['qty'])

    assert data['expected'] == cart_qty, data['message']
