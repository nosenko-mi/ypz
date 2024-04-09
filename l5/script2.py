from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from math import log, sin
import random


def suninjuly(driver: webdriver):

    driver.get('http://suninjuly.github.io/math.html')

    x = int(driver.find_element(By.ID, 'input_value').text)

    # ln(abs(12*sin(x)))

    y = log(abs(12 * sin(x)))

    answer_field = driver.find_element(By.ID, 'answer')
    answer_field.send_keys(y)

    robot_checkbox = driver.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robots_rule_button = driver.find_element(By.ID, 'robotsRule')
    robots_rule_button.click()

    answer_field.submit()

    # driver.quit()


def fill_info(driver, fn, ln, email, password):
    try:
        driver.find_element(By.ID, 'firstname').send_keys(fn)
        driver.find_element(By.ID, 'lastname').send_keys(ln)
        driver.find_element(By.ID, 'email_address').send_keys(email)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'confirmation').send_keys(password)
        driver.find_element(
            By.CSS_SELECTOR, '#form-validate > div.buttons-set > button').click()
        return 1
    except Exception as e:
        print(e)
        return -1


def get_info():
    first_name = 'automated'
    last_name = 'test'
    random_int = random.randint(0, 999)
    email = f'{first_name}{last_name}{random_int}@gmail.com'
    password = f'{first_name}{last_name}{random_int}'

    return first_name, last_name, email, password


def create_account(driver: webdriver):
    driver.get('http://demo-store.seleniumacademy.com/customer/account/create/')

    is_account_created = False
    while not is_account_created:
        first_name, last_name, email, password = get_info()
        fill_info(driver, first_name, last_name, email, password)
        try:
            WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'error-msg')))
        except:
            is_account_created = True

    driver.back()
    # driver.quit()


def book(driver: webdriver):
    driver.get('http://suninjuly.github.io/explicit_wait2.html')

    expected_price = "$100"

    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), expected_price)
    )

    driver.find_element(By.ID, "book").click()

    x = int(driver.find_element(By.ID, 'input_value').text)
    y = log(abs(12 * sin(x)))
    driver.find_element(By.ID, 'answer').send_keys(y)
    driver.find_element(By.ID, 'solve').click()

    # driver.quit()


driver = webdriver.Chrome()
suninjuly(driver)
# book(driver)
# create_account(driver)
