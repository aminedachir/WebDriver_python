from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')$

product = input("complete name of product :")

driver.get("https://www.aliexpress.com/")