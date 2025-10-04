from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# set up driver for chrome
driver = webdriver.Chrome()
# Open a Web Page
driver.get('https://www.google.com/')
print('Page Title',driver.title)

assert 'Google' in driver.title # Testcase

# find the search Box
search_box= driver.find_element(By.NAME,"q")
search_box.send_keys("selenium python")
search_box.send_keys(Keys.ENTER)

time.sleep(3)

print("Page Title",driver.title)

driver.close()


