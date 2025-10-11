## Code-Coverage

- To measure code coverage of your code you can use diffrent packages.
- for python we can use pytest-cov.
- It ill tell what percentage of your code is tested and which lines weren't executed during test case.

- To implement that create folder named code-coverage as shown here
- create 2 files fb_login.py and test_fb_title.py 

**fb_login.py**
```py
from selenium import webdriver

def get_facebook_title():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    title= driver.title
    driver.quit()
    return title

# print('Title: ', get_facebook_title() )
# This is to just check cod eis working fine or not
```
**test_fb_title.py**
```py
from fb_login import get_facebook_title

def test_facebook_title():
    assert "Facebook" in get_facebook_title()
```

- install pytest-cov module
```bash
pip install pytest-cov
pytest --cov=fb_login # it will detect all test files associated with fb_login

pytest --cov=fb_login test_fb_title.py #for perticular file coverage

#generate HTML DOC

pytest --cov=fb_login --cov-report=html
# it will create html folder you can open index.html in browser and check
# overall coverage by file, by class etc...

# for prev session 21 if you want to check coverage for all files
pytest --cov  # check the output

```