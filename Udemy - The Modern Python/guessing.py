# Better version with function and global variable

# import random
# guess = str(random.randrange(0,10))
# print(guess)
# def play():
#     user = input("Guess a number between 1-10: ")
#     while user != guess:
#         if user < guess:
#             print("Too low, try again!")
#             user = input("Guess a number between 1-10: ")
#         elif user > guess:
#             print("Too high, try again!")
#             user = input("Guess a number between 1-10: ")
#     print("Correct!")
#     global cont
#     cont = input("Do you want more? (y/n): ").lower()
# play()
# while cont:
#     if cont == "n":
#         print("Thanks For Playing, Goodbye!")
#         break
#     elif cont == "y":
#         play()

# Basic varsion
import random

guess = str(random.randrange(0, 10))

while True:
    user = input("Guess a number between 1-10: ")
    if user < guess:
        print("Too low, try again!")
    elif user > guess:
        print("Too high, try again!")
    else:
        print("You won!")
        cont = input("Wanna play again? (y/n) ").lower()
        if cont == "y":
            guess = str(random.randrange(0, 10))
            user = None
        elif cont == "n":
            print("Thanks For Playing!")
            break
