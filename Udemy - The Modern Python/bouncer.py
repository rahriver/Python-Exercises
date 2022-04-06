# ask for age
# 18 -21 wristband
# +21 drink
# otherwise, too young, sorry
# nested conditions

age = input("How old are you?\n")
if age:
    # dont put this line before the condition, if you turn age into an int before the condition, if input is empty, you would get an error becuz empty string cant be converted into an integer.
    age = int(age)
    # we cant put the second elif age >= 18 in here because they run if the first if condition is true.
    if age >= 21:
        print("Enter and drink!")
    elif age >= 18:
        print("You have a wristband, go and party but no drinks for you!")
    else:
        print("You're too young to enter or drink, sorry!")
elif age == "":
    print("Say it!")
