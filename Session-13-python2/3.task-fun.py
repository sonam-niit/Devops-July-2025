username = input("enter your username: ")
password = input("enter your password: ")

def verify(username, password):
  if username == "admin" and password == "admin123":
    print("Login successful")
  else:
    print("Invalid credentials.")

verify(username, password)
