stored_username = "joesunnyk"
stored_password = "Apple"

username = input("Enter your username: ")
password = input("Enter your password: ")
premium_member = input("\nAre you a premium member? (Yes/No): ").lower()

if username == stored_username and password == stored_password and premium_member == "yes":
    print("\nLogin Successful!\n")
    print(f"Welcome Premium Member! {username}")
else:
    print("Access Denied!")
