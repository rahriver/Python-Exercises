# for 4 and 13, print "x is unlucky"
# for even numbers, print "x is even"
# for odd numbers, print "x is odd"
# loop through numbers 1-20 inclusive

# user = input("Number: ")

# if user:
#     user = int(user)
#     if user == 4 or user == 13:
#         print(f"{user} is Unlucky!")
#     elif user % 2 == 0:
#         print(f"{user} is even")
#     else:
#         print(f"{user} is odd")
# else:
#     print("Please enter an integer")

for i in range(1, 21):
    if i == 4 or i == 13:
        print(f"{i} is Unlucky!")
    elif i % 2 == 0:
        print(f"{i} is even!")
    else:
        print(f"{i} is odd")
