import requests

BASE_URL="https://jsonplaceholder.typicode.com/users"

data={
    "name":"sonam",
    "username":"sonam123",
    "email":"sonam-soni@gmail.com" #test-email
}
response=requests.post(BASE_URL,json=data)
# i want to register with given data in json format to this API

print(response.json())
print(response.status_code) 
# if post req done successfully then status code is 201 (created)
# get put delete (200 OK )