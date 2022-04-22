string = input('String: ').split(' ')
numbers = ('1','2','3','4','5','6','7','8','9')
digits = 0
letters = 0
for i in string:
    for j in i:
        if j in numbers:
            digits+=1
        else:
            letters+=1

print(f"LETTERS {letters}\nDIGITS {digits}")

