
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('https://www.youtube.com/watch?v=_CUaON7DQDI')
#time.sleep(1)
#driver.refresh()

watch_vedio = driver.find_element(By.CSS_SELECTOR, '#movie_player > div.ytp-cued-thumbnail-overlay > button')
watch_vedio.click()