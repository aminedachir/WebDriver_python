
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

youtube_vedio_url = input("enter your url vedio :")

driver.get(youtube_vedio_url)
watch_vedio = driver.find_element(By.CSS_SELECTOR, '#movie_player > div.ytp-cued-thumbnail-overlay > button')
watch_vedio.click()

for i in range(100):
    time.sleep(3)
    driver.refresh()
