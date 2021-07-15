from selenium import webdriver

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('https://www.paypal.com/dz/signin')

phone_number = input("Enter a phone number : ")

phone_number_input = driver.find_element()