from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

product = input("complete name of product :")

driver.get("https://www.aliexpress.com/")
time.sleep(2)

pub1 = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(14) > div > div._1-aaU > div._1ZwH_ > div.undefined._1-SOk')
pub1.click()

pub = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(16) > div > div > img.btn-close')
pub.click()

search_for_product = driver.find_element(By.CLASS_NAME, 'search-key')
search_for_product.send_keys(product)


