from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('https://www.paypal.com/dz/signin')

phone_number = input("Enter a phone number : ")

phone_number_input = driver.find_element(By.CSS_SELECTOR, '#email')
phone_number_input.send_keys(phone_number)

submit = driver.find_element(By.CSS_SELECTOR, '#btnNext')