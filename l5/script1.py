from selenium import webdriver
from selenium.webdriver.common.by import By
import os


driverLocation = "D:/webdrivers/geckodriver-v0.34.0-win64"
os.environ["webdriver.gecko.driver"] = driverLocation
driver = webdriver.ChromiumEdge()

driver.get("http://demo-store.seleniumacademy.com/")

search_field = driver.find_element(By.NAME, 'q')
search_field.clear()
search_field.send_keys('Shirts')
search_field.submit()

products = driver.find_elements(By.XPATH, "//h2[@class='product-name']/a")

print('Found ' + str(len(products)) + ' products:')
for product in products:
    print(product.text)

driver.quit()
       