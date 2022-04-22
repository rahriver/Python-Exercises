evens = ('2','4','6','8')

l = [str(x) for x in range(1000,3001)]
k = []
for i in l:
    if i[0] in evens and i[1] in evens and i[2] in evens and i[3] in evens:
        k.append(i)

print(','.join(k))
