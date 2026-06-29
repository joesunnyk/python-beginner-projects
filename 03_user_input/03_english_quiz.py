print("Read the following questions and mark them if they're True/False:\n")
score = 0
answer = input("1. There are 26 letters in English language. (True/False): ")
if answer. lower() == "true":
    score += 1
answer = input("2. There are 5 vowels in English language. (True/False): ")
if answer. lower() == "true":
    score += 1
answer = input("3. There are 20 consonants in English. (True/False): ")
if answer. lower() == "false":
    score += 1
answer = input("4. There are 9 parts of speech. (True/False): ")
if answer. lower() == "false":
    score += 1
answer = input("5. English is a non phonetic language. (True/False): ")
if answer. lower() == "true":
    score += 1
print(f"\nYour score: {score}/5\n")
if score >= 3:
    print("Congratulations! You have passed the test.")
if score <= 2:
    print("\nOops! You didn't pass the test. Better luck next time.")