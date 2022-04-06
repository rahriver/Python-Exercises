from random import choice

#------Options------#


def random_choice():
    options = ['r', 'p', 's']
    global computer
    computer = choice(options)
    global player
    player = input("(R)ock, (P)aper, (S)cissors, (Q)uit: ").lower()


def play():

    #------Scores------#
    global playerScore
    playerScore = 0
    global computerScore
    computerScore = 0
    global winScore
    winScore = 3

    while playerScore < 3 and computerScore < 3:
        random_choice()
        if computer == player:
            print("Tie!")
        elif computer == 'r' and player == 'p':
            print("You Win!")
            playerScore += 1
        elif computer == 'r' and player == 's':
            print("Computer Wins!")
            computerScore += 1
        elif computer == 'p' and player == 'r':
            print("Computer Wins!")
            computerScore += 1
        elif computer == 'p' and player == 's':
            print("You Win!")
            playerScore += 1
        elif computer == 's' and player == 'r':
            print("You Win!")
            playerScore += 1
        elif computer == 's' and player == 'p':
            print("Computer Wins!")
            computerScore += 1
        elif player == 'q':
            q = input("Are you sure you want to quit? (y/n): ").lower()
            if q == 'y':
                break
        print(f"Player: {playerScore}\nComputer: {computerScore}")
    print(
        f"------Final Score------\nPlayer {playerScore} - {computerScore} Computer")
    if playerScore > computerScore:
        print("Player Wins!")
    elif computerScore > playerScore:
        print("Computer Wins!")
    else:
        print("It's A Tie!")


play()
