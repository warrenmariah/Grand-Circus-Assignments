print("Learn your squares and cubes!")
user_integer = int(input("Enter an integer:"))
number = 0
while user_integer != 0:
    table_values = [(number, number ** 2, number ** 3)]
    print(f"{'Number':<8} {'Squared':<8} {'Cubed':<8}")
    print("=" * 25)
    for number, squared, cubed in table_values:
        print(f"{number:<8} {squared:<8} {cubed:<8}")
    for number in range(1, user_integer + 1):
        print(f"{number:<8} {number ** 2:<8} {number ** 3:<8}")
        number += 1
    break
while True:
    additional_integer = input("Continue? (y/n)")
    if additional_integer == "y":
        user_integer = int(input("Enter an integer:"))
        while user_integer != 0:
            table_values = [(number, number ** 2, number ** 3)]
            print(f"{'Number': <8} {'Squared': <8} {'Cubed'}: <8")
            print("=" * 25)
            for number, squared, cubed, in table_values:
                print(f"{number:<8} {squared:<8} {cubed:<8}")
            for number in range(1, user_integer + 1):
                print(f"{number:<8} {number ** 2:<8} {number ** 3:<8}")
                number += 1
    else:
        break
