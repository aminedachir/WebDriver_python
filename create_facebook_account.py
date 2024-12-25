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

def verif(val=3):
    if val <= 0:
        return
    try:
        verification = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="code_in_cliff"]'))
        )
        verification.send_keys("hello")
        print("Text entered successfully!")
        driver.execute_script("window.open('https://gmail.com');")
        email_ver = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
        email_ver.send_keys("aminedachri07@gmail.com")
        time.sleep(2) 
    except NoSuchElementException:
        time.sleep(2) 
        verif(val - 1)

verif()

time.sleep(100)


driver.quit()
