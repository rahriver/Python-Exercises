binary_input = input('Binary: ')
reverse = binary_input[::-1]
summation = []
l = []
n = 1
i = 0
while i < len(reverse):
    l.append(n)
    n *= 2
    i += 1

z = list(zip(reverse, l))

print(z)
for i in range(len(z)):
    summation.append(z[i][1])

print(sum(summation))
