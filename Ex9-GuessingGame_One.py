#Huy Nguyen
#Date Created: 2023-10-25
#Last Updated: 2023-10-25

#Requirement: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

NUM_ATTEMPTS = 3
ATTEMPT_VAL = [1,2,3,4,5,6,7,8,9]

while True:
    name = input('What\'s your name? ')
    if name == '':
        name = 'Potato'
    print(f'Your name is {name}\n')

    while True:
        try:
            seedVal = int(input('Please enter a number: '))
        except ValueError:
            print('The input was not a valid integer.\n')
        else:
            print(f'\nYour seed is {seedVal}\n')
            break
    
    random.seed(seedVal)
    correctVal = random.randint(1, 9)
    
    print('The computer will pick a value between 1 to 9, you have 3 attempts to guess said value.\n')
    print()
    check = True
    currentAttempt = 1
    
    while check == True and currentAttempt <= NUM_ATTEMPTS:
        try:
            print(f'Attempt {currentAttempt}\n')
            inputVal = int(input('Please enter your guess (1-9): '))
        except ValueError:
            print('The input was not a valid integer.\n')
        else:
            try:
#FIXME: bound = inputVal in 
            print(f'You entered {inputVal}\n')
            print()
            
            if inputVal == correctVal:
                print(f'Your guess was correct!\n')
                check = False
            else:
                print(f'Incorrect answer, you have {NUM_ATTEMPTS - currentAttempt} left\n')
                currentAttempt += 1
    
    print()
    endGame = input('Game Over! Do you wish to continue? [y/n]')
    
    if endGame == 'n':
        break   