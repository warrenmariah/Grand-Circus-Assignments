student_info = [
  {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
  {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
  {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]
student_name = [student_info[0]["name"], student_info[1]["name"], student_info[2]["name"]]
student_hometown = [student_info[0]["hometown"], student_info[1]["hometown"], student_info[2]["hometown"]]
student_food = [student_info[0]["favorite_food"], student_info[1]["favorite_food"], student_info[2]["favorite_food"]]


def list_names(student_name):
    student_name = [student_info[0]["name"], student_info[1]["name"], student_info[2]["name"]]
    for index, value in enumerate(student_name, start=1):
        print(f"{index}. {value}")


def get_new_student():
    new_name = input("Please input a new name for the student:")
    new_hometown = input("Next, please input their hometown:")
    new_food = input("Lastly, please input their favorite food:")
    student_info.append(get_new_student())
    return student_info


action = input("Please select which action you'd like to do (add, view, or quit):")

if action == "view":
    print(list_names([student_info]))
    student_inquiry = int(input(f"Which student would you like to learn more about? Enter a number 1-{len(student_name)}:"))
    print(f"Student {student_inquiry} is {student_name[int(student_inquiry) - 1]}. What would you like to know?")
    response = input("Enter hometown or favorite food:")
    if response == "hometown":
        print(f"{student_name[int(student_inquiry) - 1]} is from {student_hometown[int(student_inquiry) - 1]}")
    if response == "favorite food":
        print(f"{student_name[int(student_inquiry) - 1]}'s favorite food is {student_food[int(student_inquiry) - 1]}")
elif action == "add":
    print(get_new_student())
    student_name.append(get_new_student())
    student_hometown.append(get_new_student())
    student_food.append(get_new_student())
    new_list = list_names([student_info]) + get_new_student()
    action = input("Please select which action you'd like to do (add, view, or quit):")
else:
    print("Goodbye!")
