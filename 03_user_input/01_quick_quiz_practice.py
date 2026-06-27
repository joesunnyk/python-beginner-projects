# quick Quiz True of False 
print("Read the following and mark whether True or False\n")
score = 0
answer = input("1. There are twelve parts of speech in English. (True.False): ")
if answer == "True":
    score += 1

answer = input("2. There are 26 letters in English alphabet. (True/False): ")
if answer == "True": 
    score += 1

answer = input("3. English is a phonetic language. (True/False): ")
if answer == "False":
    score += 1

answer = input("4. There are 5 vowel letters in English. (True/False): ")
if answer == "True":
    score += 1

answer = input("5. There are 21 consonant letters in English. (True/False): ")
if answer == "True": 
    score += 1

print("\nYour answers have been successfully registered!")
print(f"Your score: {score}/5")

#What's your name practice?
name = input("What's your name?")
print(f"My name is {name}. Nice to meet you! My name is Arjun.")