from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('https://www.paypal.com/authflow/password-recovery/?country.x=DZ&locale.x=en_US&redirectUri=%252Fsignin%253FZ3JncnB0%253D%2526cHJwPXJwdA%253D')

phone_number = input("Enter a phone number : ")

phone_number_input = driver.find_element(By.CSS_SELECTOR, '#email')
phone_number_input.send_keys(phone_number)

submit = driver.find_element(By.CSS_SELECTOR, '#content > div:nth-child(1) > div > form > div.action > input')
submit.click()

try:
    phone = driver.find_element(By.CSS_SELECTOR, '#challenges > div > div.action > button')
    phone.click()
except NoSuchElementException:
    print("FLASE")