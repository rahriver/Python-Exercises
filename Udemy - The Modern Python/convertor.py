user = float(input("How many kilometer did u run today?\n"))
MILE = 0.621371
conv = user * MILE
rnd = round(conv)
print(f"Today you ran {conv} miles rounded to {rnd}")
