# Make it lowercase so R and r are the same value.
import random
pw = "You Win!"
cw = "CPU Wins!"
eq = "Tie!"
ps = 0
cs = 0
win = 3
score = f"------{ps} - {cs}------"
while ps < win or cs < win:
    player = input("(R)ock, (P)aper, (S)cissors / (Q)uit \n").lower()
    if player == comp:
        print(eq)
    elif player == "r":
        if comp == "s":
            ps += 1
            print(pw)
        elif comp == "p":
            cs += 1
            print(cw)
    elif player == "p":
        if comp == "s":
            cs += 1
            print(cw)
        elif comp == "r":
            ps += 1
            print(pw)
    elif player == "s":
        if comp == "r":
            cs += 1
            print(cw)
        elif comp == "p":
            ps += 1
            print(pw)
    elif player == "q":
        end = input("Do you wanna quit? (y/n): ").lower()
        if end == "y":
            break
    else:
        print("Please enter a valid move")
