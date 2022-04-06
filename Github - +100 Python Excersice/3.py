n = int(input("Number: "))

# DC, enumerate, .items()
# double = {k:v*v for k,v in dict(enumerate(range(1,n+1),start=1)).items()}
# print(double)

# zip, LC
# double = dict(zip([x for x in range(1,n+1)], [x*x for x in range(1,n+1)]))
# print(double)

# map, zip, LC
# double = dict(zip(range(1,n+1),map(lambda x: x*x,[x for x in range(1,n+1)])))
# print(double)

# for loop, .update()
# double = {}
# for i in range(1,n+1):
#     double.update({i:i*i})
# print(double)

# for loop
double = {} 
for i in range(1,n+1):
    double[i]=i*i
print(double)

