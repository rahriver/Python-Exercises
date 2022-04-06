primary = input("Do you have containers of multiple sizes?(y/n): ").lower()
DEPOSIT_LESS_ONE = 0.10
DEPOSIT_MORE_ONE = 0.25

while primary:
    if primary == "n":
        cont1 = float(input("How many containers do you have?: "))
        size = float(input("How much it weighs?: "))
        if size <= 1:
            deposit1 = cont1 * DEPOSIT_LESS_ONE 
            # you can use the code below to show as many decimal points as you want.
            print("Your deposit is " + "%.2f" % deposit1 + "$")
            break
        elif size >= 1:
            deposit2 = cont1 * DEPOSIT_MORE_ONE
            print("Your deposit is " + "%.2f" % deposit2 + "$")
            break
        else:
            print("Please enter a valid value!")
            break
    elif primary == "y":
        cont2 = float(input("Enter the number of 1 liter or less container you have: "))
        cont3 = float(input("Enter the number of 1 liter or more container you have: "))
        deposit3 = cont2 * DEPOSIT_MORE_ONE + cont3 * DEPOSIT_MORE_ONE
        print("Your deposit is " + "%.2f" % deposit3 + "$")
        break
    else:
        print("Plese enter a valid number!")
        break



