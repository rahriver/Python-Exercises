from math import sqrt as sqr

# numbers = input('Numbers Separated Bye Comma: ').split(',')
# D = []
# for i in numbers:
#     D.append(int(i))
# C = 50
# H = 30
# for i in D:
#     print(round(sqr((2 * C * i ) / H)))

C = 50
H = 30
D = [str(round(sqr((2*C*int(i))/H))) for i in input('Numbers: ').split(',')]
print(','.join(D))
