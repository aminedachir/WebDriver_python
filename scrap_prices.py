from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://demostore.supersqa.com')

all_product = driver.find_elements(By.CLASS_NAME, 'product')
print(len(all_product))