import requests

BASE_URL="https://jsonplaceholder.typicode.com/users/1"
response=requests.get(BASE_URL)
data= response.json()
print('Name: ',data['name'])
print('UserName: ',data['username'])
print('Address: ',data['address']['street'],
      data['address']['city'])

# to run set up venv
# python3 -m venv myenv
# source myenv/bin/activate
# install dependency: pip install requests
# run : python3 06.requests.py


# sudo apt install python3 python3-venv python3-pip