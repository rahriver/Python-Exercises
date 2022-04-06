import random


def flip():
    options = ['Head', 'Tail']
    return random.choice(options)


print(flip())
