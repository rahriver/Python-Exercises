# Make it lowercase so R and r are the same value.
import random

options = ["r", "s", "p"]
user1 = input("User1:\n(R)ock, (P)aper, (S)cissors\n").lower()
user2 = random.choice(options)
print(user2)

u1w = "User 1 Wins!"
u2w = "User 2 Wins!"

if user1 == "r" and user2 == "p":
    print(u2w)
elif user1 == "r" and user2 == "s":
    print(u1w)
elif user1 == "p" and user2 == "s":
    print(u2w)
elif user1 == "p" and user2 == "r":
    print(u1w)
elif user1 == "s" and user2 == "r":
    print(u2w)
elif user1 == "s" and user2 == "p":
    print(u1w)
else:
    print("Tie!")
