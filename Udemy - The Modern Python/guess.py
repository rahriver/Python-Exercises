def guesser(guess,user_guess,a,b):
    if user_guess=="d":
        (a,b)=(-1,-1)
    elif user_guess=="k":
        (a,b)=(a,guess)
    elif user_guess=="b":
        (a,b)=(guess,b)
    return(a,b)
from random import randint
a=1
b=99
last_guess=0
guess=randint(a,b)
print(guess)
user_guess=input()
while True:
    (a,b)=guesser(guess,user_guess,a,b)
    if (a,b)==(-1,-1):
        break

    guess=randint(a,b)

    if last_guess==last_guess:
        guess=randint(a,b)
    if last_guess==last_guess:
        guess=randint(a,b)

    print(guess)
    user_guess=input()
