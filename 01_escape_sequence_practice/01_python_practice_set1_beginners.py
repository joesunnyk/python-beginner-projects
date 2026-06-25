#Q1. Write your first program.
#Write a program that prints: Hello, World! Welcome to Python.
print("1. My First Python Program")
print("Hello, world!", "Welcome to Python.")

#2. Print a Poem.
#Write a program that prints the following peom using a single print() statement:
print("\n2. My First Poem in Python")
print("Twinkle", "Twinkle", "Little Star", "\nHow I wonder what you are", sep=", ", end="!")

#3. Variables and Data Types

print("\n\n3. Creating variables to store:- \n-your name(string) \n-your age(integer) \n-your height in meters(float) \n-A boolean value representing whther you are a student. \nprint all of them in one line")
name, age, height, is_student = "Joe Sunny", 35.6, 5.5, True 

#4. Typecasting Practice
print("\n\n4. Typecasting Practice")
print("You're given a string:")
print("num = 45")
print("Convert it into an integer and add 10 to it. Print the result.")
print("\nThe given number as string is num = '45'. " \
"So I have taken a variable of 'number' and assigned 'int' data type to convert it to an integer and I added 10 to the created data type 'int' and I printed the result.")
num = "45"
number = int(num)
print(number+10)

#5. Taking User Input:
print("\n\n5. Taking User Input")
print("\nWriting a program that:")
print("1. Asks the user for their favourite food.")
print("2. Prints: wow! I also like <food>.")

print("\nHere's the answer1...")
food = input("What's your favourite food?")
print(f"My favourite food is {food}. Wow! I also like {food}.")

print("\nPrint User Answer2")
name = input("What's your name?")
print(f"My name is {name}. Nice! I'm Joe. Nice meeting you!")
