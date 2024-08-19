def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed == True:
        print(
            f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month...")
    else:
        print(
            f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month... ")


print(apt_search1("Atlanta", 2000, 2, True))
print(apt_search1("Walla Walla", 1500, 1, False))


def apt_search2(city, max_rent, min_beds, pets_allowed):
    if min_beds == 0 and pets_allowed != True:
        print(f"Welcome to GC Property Management! Looking up listings in {city} all within a budget of ${max_rent} per month...")
    elif min_beds == 0 and pets_allowed == True:
        print(f"Welcome to GC Property Management! Looking up listings in {city} that allows pets, all within a budget of ${max_rent} per month...")
    elif min_beds != 0 and pets_allowed != True:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...")


print(apt_search2("Charlotte", 1500, min_beds=0, pets_allowed=False))
print(apt_search2("Charlotte", 1500, 1, False))
print(apt_search2("Charlotte", 1500, min_beds=0,pets_allowed=True))

plus_one_hundred = lambda x: x + 100
square_num = lambda x: x ** 2
phrase = "hello"
concatenate = lambda string: f"- {phrase}"
divide_by_three = lambda x: x / 3

print(plus_one_hundred(30))
print(square_num(4))
print(concatenate(phrase))
print(divide_by_three(9))
