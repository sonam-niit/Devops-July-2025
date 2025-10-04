from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# set up driver for chrome
driver = webdriver.Chrome()
# Open a Web Page
driver.get('https://www.facebook.com/')
driver.find_element(By.ID,"email").send_keys("sonam@gmail.com")
driver.find_element(By.ID,"pass").send_keys("123456789")
driver.find_element(By.NAME,"login").click()
time.sleep(5)
driver.quit()