from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

service = Service(executable_path="/home/aminedachir/Documents/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/r.php?entry_point=login")
input_element = driver.find_element(By.NAME,"firstname")
input_element.send_keys("nima")

input_element = driver.find_element(By.NAME,"lastname")
input_element.send_keys("dima")

day  = driver.find_element(By.NAME,"birthday_day")
select_day = Select(day)
select_day.select_by_value("1")

month  = driver.find_element(By.NAME,"birthday_month")
select_month = Select(month)
select_month.select_by_value("3")

year  = driver.find_element(By.NAME,"birthday_year")
select_year = Select(year)
select_year.select_by_value("1998")

gender = driver.find_elements(By.CLASS_NAME, "_8esa")
gender[1].click()

email = driver.find_element(By.NAME,"reg_email__")
email.send_keys("aminedachri07@gmail.com")

password = driver.find_element(By.NAME,"reg_passwd__")
password.send_keys("By@moi005")

signup = driver.find_element(By.NAME,"websubmit")
signup.click()

#try:
 #   continu = driver.find_element(By.CLASS_NAME,"x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3")
  #  print("we found a capatcha problem \n please enter the capatcha")
#except NoSuchElementException:
 #   print("no")

time.sleep(10)

driver.quit()
