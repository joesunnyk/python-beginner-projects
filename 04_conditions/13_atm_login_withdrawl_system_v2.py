print("=================================\n")
print("\tWelcome! ABC Bank\n")
print("=================================\n")

stored_card = 123456789
stored_pin = 8742
balance = 5000

card_number = int(input("Enter your card number: "))
pin_number = int(input("Enter your PIN number: "))
if card_number == stored_card and pin_number == stored_pin:
    withdrawal_amount = int(input("Enter your withdrawal amount:₹ "))
    if withdrawal_amount > balance:
        print("Insufficient balance!")
    else:
        balance -= withdrawal_amount
        print(f"\n₹{withdrawal_amount} has been withdrawn successfully!")

        answer = input("Do you want to check your balance? (Yes/No): ").lower()
        if answer == "yes":
            print(f"Your available balance is ₹{balance}.")
        else:
            print("Thank you for choosing ABC bank!")
else:
    print("\nInvalid card number or PIN")