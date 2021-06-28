from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://127.0.0.1:5000/')

email_field = driver.find_element(By.ID, 'email')
email_field.send_keys("dachiramine0@gmail.com")
driver.close()
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys("amineamine")
password_field.send_keys(Keys.ENTER)

multiplication = driver.find_element(By.CSS_SELECTOR, 'body > fieldset > div > a:nth-child(3)')
multiplication.click()
