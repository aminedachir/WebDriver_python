from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

try:
  verification = WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.XPATH,'//*[@id="code_in_cliff"]'))
  )
  verification.send_keys("hello")
  print("Text entered successfully!")
  driver.execute_script("window.open('https://gmail.com');")
  gmail_window = driver.window_handles
  driver.switch_to.window(gmail_window[1])
  print(driver.title)
  email_ver = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]'))
  )
  email_ver.send_keys("aminedachri07@gmail.com")
  next_ = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')
  next_.click()
  pass_ver = WebDriverWait(driver,30).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input'))
  )
  pass_ver.send_keys("hello")
  next_ = driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
  next_.click()
except NoSuchElementException:
  time.sleep(2) 
  print("no")
time.sleep(100)

driver.quit()