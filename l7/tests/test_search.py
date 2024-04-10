from main_page import MainPage
import sys
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append("D:/Programming/znu/ypz/l7/pages")

test_data = [
    {"category": "Denim", "expected": 2,
        "message": "Number of denim product shoul be 2."},
]


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/')
    yield browser
    browser.quit()


@pytest.mark.parametrize("data", test_data)
def test_sarch_with_data(browser, data):

    page = MainPage(browser)
    real_number = page.search_with_data(data['category'])

    assert data['expected'] == real_number, data['message']
