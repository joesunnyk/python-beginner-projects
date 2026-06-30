card_number = input("Enter your card number: ")
pin = input("Enter your PIN: ")
withdrawl_amount = input("Enter the withdrawal amount: ")
if card_number and pin:
    print(f"Here's the amount withdrawn {withdrawl_amount}.")
else:
    print("Card number or PIN is invalid. Please try again!")

answer = input("Do you want to check your current balance? (Yes/No): ").lower()
if answer == "yes":
    print(" Click Here to check your balance.")
else:
    print("Thank you for choosing ABC bank!")