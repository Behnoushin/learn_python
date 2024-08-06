import random
pc_number = random.randint(1,99)
your_number = input('pleas inter your number (1,99)---> ')
def baziii():
    while(True):
        if pc_number == your_number:
            print ('You guessed it right')
        else:
            print ('try again')
            break 
baziii()
