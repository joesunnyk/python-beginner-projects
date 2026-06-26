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
print(f"My name is {name}. Nice! I'm Joe. Nice meeting you!\n")

#6. A Simple caliculator project
print("\n6. Programming a little caliculator")
a = int(input("enter first number\n"))
b = int(input("enter second number\n"))

print("a+b is ", a+b)
print("a-b is ", a-b)
print("a/b is ", a/b)
print("a*b is ", a*b)

#6.1 Asimple caliculator project 2
print("6.1 A simple caliculator project 2")
c = int(input("enter first number"))
d = int(input("enter second number"))

print("c+d is ", c+d)
print("c-d is ", c-d)
print("c*d is ", c*d)
print("c%d is", c%d)

#7. Escape sequence practice
print("\nEscape sequence practice")
print('Harry said, "Python is awesome!"\nThis is on a newline.\nThis is a tab ->\t<- here')

#8 Operator challenge practice
print("8. Operator challenge practice")
a = int(input("enter first number"))
print("square is", a**2)
print("cube is", a**2)

#9. A quick quiz - True or False
print("-------------------------------")
print("9. A quick Quiz - True/False")
print("-------------------------------\n")
score = 0

answer = input("1. Python code must always end with a (;). (True/False): ")
if answer == "False":
    score =+ 1

answer = input("2. The # symbol is used for comments in python. (True/False): ")
if answer == "True":
    score =+1

answer = input('3. "123" and 123 are the same in python. (True/False):')
if answer == "False":
    score =+1

answer = input("4. The * operator is used for multiplication. (True/False): ")
if answer == "True":
    score =+1

answer = input("5. Creates a newline. (True/False): ")
if answer == "True":
    score =+1

answer = input("6. Variables in python can start with numbers.(True/False): ")
if answer == "False":
    score =+ 1

answer = input('7. int("10") + 5 gives 15. (True/False): ')
if answer == "True":
    score =+ 1

print("----------------------------------\n")
print("\tQuick quiz completed successfully.")
print("Your score: ", score, "/7")
print("Thank you for taking the quiz")
print("-----------------------------------")
