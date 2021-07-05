
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')
driver.get('https://www.youtube.com/watch?v=2-Zfr84-H7s')
watch_vedio = driver.find_element(By.CSS_SELECTOR, '#movie_player > div.ytp-cued-thumbnail-overlay > button')
watch_vedio.click()
for i in range(100):
    time.sleep(2)
    driver.refresh()