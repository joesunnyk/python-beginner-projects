#1. Personal Introuction
print("Personal Introduction exercise 1\n")
name = input("What's your name? ")
age = input("How old are you? ")
city = input("Where do you live? ")
print(f"Hello! {name}\n")
print(f"You are {age} years old.")
print(f"You live in {city}.\n")
print("Nice to meet you!")

# #Exercise 2 - Student Information
print("Taking Student Information Exercise 2")
studentname = input("Enter you name. ")
collegename = input("Enter your college name. ")
course = input("Enter your course name. ")
year = input("Enter the year of the course. ")
print("==============================\n")
print("\tStudent Information\n")
print("==============================\n")
print(f"Name:\t{studentname}")
print(f"College:\t{collegename}")
print(f"course:\t\t{course}")
print(f"Final Year:\t{year}\n")
print("==============================") 

# #Exercise 3 - The Restaurant Bill
print("Exercise 3 The Restaurant Bill\n")
customername = input("Enter Your Name:\t ")
fooditem = input("What did you eat?:\t ")
quantity = input("How many did you eat?:\t ")
price = input("What's the total cost?:\t ")
print(f"Customer:\t{customername}")
print(f"Food:\t{fooditem}")
print(f"Quantity:\t{quantity}")
print(f"Price:\t{300}\n")
print("Thank you for visiting!")

#Exercise 4: Job applicatin Form
print("Exercise 4: Job Application Form\n")
name = input(" ")
email = input(" ")
phonenumber = input(" ")
highestqualification = input(" ")
yearsofexperience = input(" ")
print("================================\n")
print("\tJob Application Form\n")
print("================================\n")
print(f"Name\t\t:{name}")
print(f"Phone Number\t:{phonenumber}")
print(f"Qualification\t:{highestqualification}")
print(f"Experience\t:{yearsofexperience}\n")
print("Application Submitted Successfully!")

# #Exercise 5 Movie Ticket Booking
print("Exercise 5 Movie Ticket Booking\n")
name = input("\t")
moviename = input("\t")
theatre = input("\t")
numberoftickets = input("\t")
print("==============================\n")
print("\tMOVIE TICKET\n")
print("==============================\n")
print(f"Name\t: {name}")
print(f"Movie\t: {moviename}")
print(f"Theatre\t: {theatre}")
print(f"Tickets\t: {numberoftickets}\n")
print("Enjoy the Movie!")

#Challenge 6 (A Little Harder)
print("Challenge 6 A little Harder\n")
name = input(" ")
source = input(" ")
destination = input(" ")
dateofjourney = input(" ")
trainnumber = input(" ")
seatpreference = input(" ")
print("===========================\n")
print("\tTravel Ticket\n")
print("===========================\n")
print(f"Passenger Name\t: {name}")
print(f"From\t\t: {source}")
print(f"To\t\t: {destination}")
print(f"Date\t\t: {dateofjourney}")
print(f"Train Number\t: {trainnumber}")
print(f"Seat\t\t: {seatpreference}\n")
print("Have a safe journey!")

#Challenge 6.1 (A Little harder version)
name = input(" ")
source = input(" ")
destination = input(" ")
dateofjourney = input(" ")
trainnumber = input(" ")
seatpreference = input(" ")

print(f"""
===================================\n
      \tTRAVEL TICKET\n
===================================\n
      Passenger Name\t: {name}\n
      From\t\t: {source}\n
      To\t\t: {destination}\n
      Date\t\t: {dateofjourney}\n
      Train Number\t: {trainnumber}\n
      Seat\t\t: {seatpreference}\n
      Have a Safe Journey!
      """)

# Challenge 7: A LinkedIn Profile Generator
print("Create a LinkedIn Profile Generator\n")
name = input(" ")
jobtitle = input(" ")
company = input(" ")
skills = input(" ")
location = input(" ")
yearsofexperience = input(" ")

print(f"""===============================\n
      \tLINKEDIN PROFILE\n
=============================== \n
      Name\t: {name}\n
      Job Title\t: {jobtitle}\n
      Company\t: {company}\n
      Skills\t: {skills}\n
      Location\t: {location}\n
      Experience: {yearsofexperience}\n
      Ready to connnect with professinoals!
 """)

#A Coffee Shop Order Form

print("A coffee Shop Order Form")

customername = input("What's your name?\t\t: ")
coffeetype = input("What's your favourite coffee?\t: ")
size = input("Which size of the coffee would you like? Small/Medium/Large\t: ")
sugar = input("Do you like sugar? Yes/No\t: ")
takeaway = input("Would you like takeaway? Yes/No\t: ")
print(f"""
=================================\n
      \t Coffee Receipt\n
=================================\n
    What's your name?\t\t\t\t\t\t: {customername}\n
    What's your favourite coffee?\t\t\t\t: {coffeetype}\n
    Which size of the coffee would you like? Small/Medium/Large\t: {size}\n
    Do you like sugar? Yes/No\t\t\t\t\t: {sugar}\n
    Would you like takeaway? Yes/No\t\t\t\t: {takeaway}\n
Enjoy Your Fresh coffee!
""")