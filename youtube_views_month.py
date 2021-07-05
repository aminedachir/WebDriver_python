from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('https://www.youtube.com/channel/UCaj2GeIsW6Xll26js9o4seQ')
videos = driver.find_element(By.CSS_SELECTOR, '#tabsContent > tp-yt-paper-tab:nth-child(4) > div')
videos.click()
all_videos = driver.find_elements(By.CSS_SELECTOR, '#meta')
print(len(all_videos))