answer = int(input("Welcome! Which student would you like to learn more about? Enter a number between 1-4:"))
student_name = ["Barry Jones", "Kim Clarke", "Natasha Johnson", "Rick Harris"]
student_hometown = ["Seattle, WA", "Charlotte, NC", "Manhattan, NY", "Honolulu, HI"]
student_food = ["General Tso Chicken", "Kimchi", "Smoothies", "Malasadas"]

if answer == 1:
    print(f"Student 1 is {student_name[0]}. What would you like to know?")
elif answer == 2:
    print(f"Student 2 is {student_name[1]}. What would you like to know?")
elif answer == 3:
    print(f"Student 3 is {student_name[2]}. what would you like to know?")
elif answer == 4:
    print(f"Student 4 is {student_name[3]}. What would you like to know?")

while answer < 1 or answer > 4:
    print("The number entered is not valid. Please enter a number between 1 and 4.")
    answer = int(input("Welcome! Which student would you like to learn more about? Enter a number 1-4:"))
    if answer == 1:
        print(f"Student 1 is {student_name[0]}. What would you like to know?")
    elif answer == 2:
        print(f"Student 2 is {student_name[1]}. What would you like to know?")
    elif answer == 3:
        print(f"Student 3 is {student_name[2]}. What would you like to know?")
    elif answer == 4:
        print(f"Student 4 is {student_name[3]}. What would you like to know?")

answer2 = input("Enter Hometown or Favorite Food:")

if answer2 == "Hometown":
    if answer == 1:
        print(f"{student_name[0]} is from {student_hometown[0]}.")
    elif answer == 2:
        print(f"{student_name[1]} is from {student_hometown[1]}.")
    elif answer == 3:
        print(f"{student_name[2]} is from {student_hometown[2]}.")
    elif answer == 4:
        print(f"{student_name[3]} is from {student_hometown[3]}.")
if answer2 == "Favorite Food":
    if answer == 1:
        print(f"{student_name[0]}'s favorite food is {student_food[0]}.")
    elif answer == 2:
        print(f"{student_name[1]}'s favorite food is {student_food[1]}.")
    elif answer == 3:
        print(f"{student_name[2]}'s favorite food is {student_food[2]}.")
    elif answer == 4:
        print(f"{student_name[3]}'s favorite food is {student_food[3]}.")

answer3 = input("Would you like to learn about another student? Enter y or n:")

if answer3 == "y":
    answer = int(input("Welcome! Which student would you like to learn more about? Enter a number 1-4:"))
    if answer == 1:
        print(f"Student 1 is {student_name[0]}. What would you like to know?")
    elif answer == 2:
        print(f"Student 2 is {student_name[1]}. What would you like to know?")
    elif answer == 3:
        print(f"Student 3 is {student_name[2]}. What would you like to know?")
    elif answer == 4:
        print(f"Student 4 is {student_name[3]}. What would you like to know?")
    while answer < 1 or answer > 4:
        print("The number entered is not valid. Please enter a number between 1 and 4.")
        answer = int(input("Welcome! Which student would you like to learn more about? Enter a number 1-4:"))
        if answer == 1:
            print(f"Student 1 is {student_name[0]}. What would you like to know?")
        elif answer == 2:
            print(f"Student 2 is {student_name[1]}. What would you like to know?")
        elif answer == 3:
            print(f"Student 3 is {student_name[2]}. What would you like to know?")
        elif answer == 4:
            print(f"Student 4 is {student_name[3]}. What would you like to know?")
    answer2 = input("Enter Hometown or Favorite Food:")
    if answer2 == "Hometown":
        if answer == 1:
            print(f"{student_name[0]} is from {student_hometown[0]}.")
        elif answer == 2:
            print(f"{student_name[1]} is from {student_hometown[1]}.")
        elif answer == 3:
            print(f"{student_name[2]} is from {student_hometown[2]}.")
        elif answer == 4:
            print(f"{student_name[3]} is from {student_hometown[3]}.")
    if answer2 == "Favorite Food":
        if answer == 1:
            print(f"{student_name[0]}'s favorite food is {student_food[0]}.")
        elif answer == 2:
            print(f"{student_name[1]}'s favorite food is {student_food[1]}.")
        elif answer == 3:
            print(f"{student_name[2]}'s favorite food is {student_food[2]}.")
        elif answer == 4:
            print(f"{student_name[3]}'s favorite food is {student_food[3]}.")
else:
    print("Thanks")
