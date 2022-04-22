net = 0
while True:
    s = input('Gimme: ')
    if not s:
        break
    val = s.split(' ')
    i = val[0]
    amount = int(val[1])
    if i == 'D':
        net += amount
    elif i == 'W':
        net -= amount
    else:
        pass
print(net)
