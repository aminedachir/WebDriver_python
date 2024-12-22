from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service(executable_path="/home/aminedachir/Documents/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/r.php?entry_point=login")
input_element = driver.find_element(By.NAME,"firstname")
input_element.send_keys("abdelghani")

input_element = driver.find_element(By.NAME,"lastname")
input_element.send_keys("djoudi")

day  = driver.find_element(By.NAME,"birthday_day")
select_day = Select(day)
select_day.select_by_value("5")

month  = driver.find_element(By.NAME,"birthday_month")
select_month = Select(month)
select_month.select_by_value("9")

year  = driver.find_element(By.NAME,"birthday_year")
select_year = Select(year)
select_year.select_by_value("1999")

gender = driver.find_elements(By.CLASS_NAME, "_8esa")
gender[1].click()

time.sleep(10000)

driver.quit()
