string = input('String: ').split(' ')
upper = 0
lower = 0

for i in string:
    for j in i:
        if j.isalpha():
            if j == j.upper():
                upper+=1
            else:
                lower+=1

print(f"UPPER CASE {upper}\nLOWER CASE {lower}")

