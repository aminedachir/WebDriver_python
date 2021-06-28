from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://127.0.0.1:5000/')

input_field = driver.find_element(By.ID, 'email')
print(input_field)
