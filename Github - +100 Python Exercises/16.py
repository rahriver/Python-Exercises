num = [x for x in input('Numbers: ').split(',')]
l = [str(int(x)**2) for x in num if int(x) % 2 != 0]
print(','.join(l))
