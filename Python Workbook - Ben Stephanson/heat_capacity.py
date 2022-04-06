mass = float(input("Enter the mass of the water in kilograms: "))
temp1 = float(input("Enter the current temp: "))
temp2 = float(input("Enter the desired temp: "))

qkg = (mass * 4186) * (temp2 - temp1)
qj = qkg/1000
print(f"The total energy of the water is: {qj} J/gC")

