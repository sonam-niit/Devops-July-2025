import re

text="hello world"

match= re.match(r"hello",text)
if match:
    print('text started with hello')
else:
    print('text not started with hello')
    
search = re.search(r"world",text)
if search:
    print('text includes world')
else:
    print('text not includes world')