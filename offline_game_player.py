from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://fb.com')
time.sleep(3)
for i in range (10):
    dayn = driver.find_element(By.CLASS_NAME, "runner-canvas")