def heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp:
        print(f"Current Temp {actual_temp}")
        print(f"Desired Temp {desired_temp}")
        print("Run Heat")
    elif actual_temp > desired_temp:
        print(f"Current Temp {actual_temp}")
        print(f"Desired Temp {desired_temp}")
        print("Run A/C")
    elif actual_temp == desired_temp:
        print(f"Current Temp {actual_temp}")
        print(f"Desired Temp {desired_temp}")
        print("Standby")


print(heating_cooling(60, 70))
print(heating_cooling(68, 65))

user_current = int(input("Enter the current temperature:"))
user_desired = int(input("Enter the desired temperature:"))
print(heating_cooling(user_current, user_desired))
