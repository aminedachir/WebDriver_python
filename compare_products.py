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

price = driver.find_element(By.CSS_SELECTOR, '#results-list > div:nth-child(1) > div > div.listing-item > div.block.item-title > div > span')
print(price.text)
color = driver.find_element(By.XPATH, '//*[@id="results-list"]/div[1]/div/div[2]/div[2]/div[2]/ul/li[2]/ul[1]/li[1]/strong')
print(color.text)
#year =
#kilometers =
#doors =
