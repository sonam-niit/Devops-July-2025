from selenium import webdriver

def get_facebook_title():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    title= driver.title
    driver.quit()
    return title

# print('Title: ', get_facebook_title() )
# This is to just check cod eis working fine or not