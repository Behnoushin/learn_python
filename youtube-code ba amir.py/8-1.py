import random

a = ["rock", "paper", "scissors"]

word = input('Enter rock, paper, or scissors: ')

def game():
    while True:
        try:
            if word not in a:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print(" You must enter rock, paper, or scissors.")
    c = random.choice(a)
    print('The computer drew ' + c )

    if c == 'rock' and word=='rock':
        print('It was a tie')
    elif c == 'paper' and word=='paper':
        print('It was a tie')
    elif c == 'scissors' and word=='scissors':
        print('It was a tie')

    elif c == 'paper' and word=='rock':
        print('you lost')
    elif c == 'rock' and word=='paper':
        print('you won!')

    elif c == 'rock' and word=='scissors':
        print('you lost')
    elif c == 'scissors' and word=='rock':
        print('you won!')

    elif c == 'scissors' and word=='rock':
        print('you won!')
    elif c == 'scissors' and word=='rock':
        print('you won!')

play_again = "yes"

while play_again == "yes":

    game()

    play_again = input('would you like to play again: ').lower()
