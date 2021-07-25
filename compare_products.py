from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

car = input("name of car :")
model = input("Model of car :")

driver.get("https://dubai.dubizzle.com/")

search_for_product = driver.find_element(By.CLASS_NAME, 'Searchbox__keyword__input')
search_for_product.send_keys(car," ", model)
search_for_product.send_keys(Keys.ENTER)

try:
    price = driver.find_element(By.CSS_SELECTOR, '#results-list > div:nth-child(1) > div > div.listing-item > div.block.item-title > div > span')
    year = driver.find_element(By.XPATH, '//*[@id="results-list"]/div[1]/div/div[2]/div[2]/div[2]/ul/li[2]/ul[1]/li[1]')
    color = driver.find_element(By.XPATH, '//*[@id="results-list"]/div[1]/div/div[2]/div[2]/div[2]/ul/li[2]/ul[2]/li[2]')
    kilometers = driver.find_element(By.XPATH, '//*[@id="results-list"]/div[1]/div/div[2]/div[2]/div[2]/ul/li[2]/ul[1]/li[2]')
    doors = driver.find_element(By.XPATH, '//*[@id="results-list"]/div[1]/div/div[2]/div[2]/div[2]/ul/li[2]/ul[2]/li[1]')
    print("Price :",price.text,",", year.text,",", color.text,",", kilometers.text,",", doors.text)
    time.sleep(1)
except NoSuchElementException:
    print("No resulte fond")

driver.get('https://uae.yallamotor.com/')