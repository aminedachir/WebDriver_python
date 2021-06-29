from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path = '/home/amine/Downloads/chromedriver')

driver.get('http://demostore.supersqa.com')

all_product = driver.find_elements(By.CLASS_NAME, 'product')
print(len(all_product))

for product in all_product:
    price_elm = product.find_element(By.CSS_SELECTOR, 'span.amount')
    price = price_elm.text

    name_elm = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    name = name_elm.text

    print(name, price)