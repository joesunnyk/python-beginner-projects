age = int(input("Enter your age: "))
student = input("Are you a student? (Yes/No): ").lower()
if age <=12 or student == "yes": 
    print("Congratulations! You're eligible for a student discount. Here is the discount code OFF50")
else:
    print("Oops! You're not eligible for the student discount.")