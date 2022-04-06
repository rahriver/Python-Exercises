emoji = "\U0001f600"
user = int(input("How many times?: "))
n = 1
while n < user:
    print(emoji*n)
    n += 1

# ugly solution
# for i in range(1,11):
#     count = 1
#     smily = ""
#     while count <= i:
#         smily += "\U0001f600"
#         count += 1
#     print(smily)
