widget = int(input("How many widgets?: "))
gizmos = int(input("How many gizmos?: "))
GIZMOS = 112
WIDGET = 75

weight = gizmos * GIZMOS + widget * WIDGET
if weight >= 1000:
    kg = weight / 1000
    print(f"Total weight of the parts is: {kg} kg")
else:
    print(f"Total weight of the parts is: {weight} grams")

