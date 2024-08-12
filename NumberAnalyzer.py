user_integer = int(input("Enter a whole number between 1 and 100:"))

if user_integer % 2 != 0 and user_integer < 60:
    print(f"{user_integer} Odd and less than 60.")
elif user_integer % 2 == 0 and 2 <= user_integer < 25:
    print(f"{user_integer} Even and less than 25.")
elif user_integer % 2 == 0 and 26 <= user_integer <= 60:
    print(f"{user_integer} Even and between 26 and 60 inclusive.")
elif user_integer % 2 == 0 and user_integer > 60:
    print(f"{user_integer} Even and greater than 60.")
elif user_integer % 2 != 0 and user_integer > 60:
    print(f"{user_integer} Odd and greater than 60.")
