number = int(input("Number: "))
if number < 0:
    print("Please enter a positive integer!")
else:
    gauss = sum(range(1,number))
    print(f"Sum of (1-{number}) is: {gauss}")
