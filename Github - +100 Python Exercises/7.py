x = int(input("X: "))
y = int(input("Y: "))
l = []
i = 0
while i < x:
    l.append([j*i for j in range(0,y)])
    i+=1
print(l)
