n = int(input("Number: "))

c = 1
i = 1
while i <= n:
    if n == 0:
        print(c)
        break
    else:
       c *= i
       i += 1

print(c)
