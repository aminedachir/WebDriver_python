
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('https://www.youtube.com/watch?v=mlZj910ey-I')

watch_vedio = driver.find_element(By.CSS_SELECTOR, '#movie_player > div.ytp-cued-thumbnail-overlay > button')
watch_vedio.click()
for i in range(100):
    time_vedio = driver.find_element(By.CSS_SELECTOR, '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span.ytp-time-duration')
    timevd = time_vedio.text
    if int(timevd[2:4] > 0):
        r = int(timevd[0:2])
    else:
        r = int(timevd[2:4])
    time.sleep(5)
    driver.refresh()