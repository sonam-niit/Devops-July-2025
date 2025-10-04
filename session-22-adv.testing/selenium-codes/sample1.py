from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://selenium.dev/documentation')
assert 'Selenium' in driver.title

elem = driver.find_element(By.ID, 'm-documentationwebdriver')
elem.click()
assert 'WebDriver' in driver.title

driver.quit()