from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://youtube.com')

print(driver.title)