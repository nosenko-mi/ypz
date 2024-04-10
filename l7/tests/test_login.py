import pytest
import os
import sys
from selenium import webdriver

sys.path.append("D:/Programming/znu/ypz/l7/pages")
from login_page import LoginPage


test_data = [
    {"email": "userexists111@gmail.com", "password": "userexists111", "element": "customer-account-index.customer-account",
        "message": "Existing user should be redirected to 'My account' page"},
    {"email": "userdoesnotexist121@gmail.com", "password": "userexists121",
        "element": "error-msg", "message": "Error message shoud pop up if user does not exist."},
    {"email": "userexists111@gmail.com", "password": "userexists222", "element": "error-msg",
        "message": "Error message shoud pop up if user does not exist."}
]


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    browser.get(
        'http://demo-store.seleniumacademy.com/customer/account/login/')
    yield browser
    browser.quit()


@pytest.mark.parametrize("data", test_data)
def test_login_with_data(browser, data):
    login_page = LoginPage(browser)
    real = login_page.login_with_data(data)
    assert real is not None, data["message"]
