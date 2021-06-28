from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://amazon.com')

covid = driver.find_element(By.ID, 'swm-link')
print(covid)
print(type(covid))
print(covid.text)

search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys("amine dachir")
search.send_keys(Keys.ENTER)