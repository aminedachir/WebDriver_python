from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

service = Service(executable_path="/home/aminedachir/Documents/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/r.php?entry_point=login")
input_element = driver.find_element(By.NAME, "firstname")
input_element.send_keys("nima")

input_element = driver.find_element(By.NAME, "lastname")
input_element.send_keys("dima")

day = driver.find_element(By.NAME, "birthday_day")
select_day = Select(day)
select_day.select_by_value("1")

month = driver.find_element(By.NAME, "birthday_month")
select_month = Select(month)
select_month.select_by_value("3")

year = driver.find_element(By.NAME, "birthday_year")
select_year = Select(year)
select_year.select_by_value("1998")

gender = driver.find_elements(By.CLASS_NAME, "_8esa")
gender[1].click()

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys("inputuser4@gmail.com")

password = driver.find_element(By.NAME, "reg_passwd__")
password.send_keys("@Descret00")

signup = driver.find_element(By.NAME, "websubmit")
signup.click()

try:
    verification = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="code_in_cliff"]'))
    )


    driver.execute_script("window.open('https://gmail.com');")
    gmail_window = driver.window_handles
    driver.switch_to.window(gmail_window[1])

    email_ver = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
    email_ver.send_keys("inputuser4@gmail.com")
    next_ = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    next_.click()

    pass_ver = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
    pass_ver.send_keys("@Descret00")
    next_ = driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
    next_.click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="aH5"]'))
    )

    emails = driver.find_elements(By.XPATH, '//div[@class="aTg"]') 
    for email_item in emails:
        if "Facebook" in email_item.text: 
            email_item.click()
            break

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Your Facebook verification code")]'))
    ) 
    email_body = driver.find_element(By.XPATH, '//*[@class="ii gt"]')  
    email_text = email_body.text
    pin = re.search(r'\d{6}', email_text)  
    if pin:
        pin_code = pin.group(0)  
        print(f"Verification PIN extracted: {pin_code}")
        driver.switch_to.window(gmail_window[0])
        pin_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="code_in_cliff"]'))
        )
        pin_input.send_keys(pin_code)
        print("PIN entered successfully!")
    else:
        print("No PIN found in the email.")
except NoSuchElementException:
    print("Captcha detected")

time.sleep(100) 
driver.quit()