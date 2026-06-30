print("Welcome to Voting Age Checker!\n")
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (Yes/No): ").lower()
if age >= 18 and citizenship == "yes": 
    print("You're allowed to vote.")
else:
    print("You're not allowed to vote.")