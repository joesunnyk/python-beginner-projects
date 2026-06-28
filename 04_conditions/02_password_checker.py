print("The Password Checker: \n")
correctpassword = input("Enter the Password: ")
if correctpassword == "Python123":
    print(f"{correctpassword} Access Granted! ✅")
else: 
    print("Access Denied! ❌ Please retry the password")
correctpassword = input("Enter the password: ")
if correctpassword == "Python123":
    print(f"{correctpassword} Access Granted! ✅")
else:
    print("Oops! Access Denied! ❌ You have one last attempt. Enter the password correctly")
correctpassword = input("Enter the password: ")
if correctpassword == "Python123": 
    print(f"{correctpassword} Great! Access Granted! ✅")
else:
    print("Oops! System crashed ⛔")