stored_username = "joe123"
stored_password = "Python123"
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == stored_username and password == stored_password:
    print("Login Successful!")
else:
    print("Invalid username or password.")