from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://127.0.0.1:5000/')

input_field = driver.find_element(By.ID, 'email')
input_field.send_keys("dachiramine0@gmail.com")
input_field.send_keys(Keys.ENTER)
print(input_field)