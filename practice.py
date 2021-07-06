from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')
driver.get('http://127.0.0.1:5000/')
time.sleep(1)
emails = ['amine@gmail.com','mohamed@gmail.com','yassin@gmail.com','ahmed@gmail.com','hichem@gmail.com']
for i in range(5):
    email = emails[i]
    email_field = driver.find_element(By.ID, 'email')
    email_field.send_keys(email)
    time.sleep(0.5)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("amineamine")
    time.sleep(0.5)
    email_field.send_keys(Keys.ENTER)
    time.sleep(0.5)
time.sleep(1)
driver.quit()
