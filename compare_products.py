from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

product = input("complete name of product :")

driver.get("https://dubai.dubizzle.com/")

search_for_product = driver.find_element(By.CLASS_NAME, 'Searchbox__keyword__input')
search_for_product.send_keys(product)
search_for_product.send_keys(Keys.ENTER)

