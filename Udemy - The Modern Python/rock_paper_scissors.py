# Make it lowercase so R and r are the same value.
user1 = input("User1:\n(R)ock, (P)aper, (S)cissors\n").lower()
# Just so user2 can't see user1's pick. but you can use random library to overcome that problem
for i in range(0, 50):
    print("******NO CHEATING******")
user2 = input("User2:\n(R)ock, (P)aper, (S)cissors\n").lower()

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
