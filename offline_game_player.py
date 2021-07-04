from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://fb.com')

dayn = driver.find_element(By.CSS_SELECTOR, "#main-frame-error > div.runner-container > canvas")