#Huy Nguyen
#Date Created: 2023-10-24
#Last Updated: 2023-10-25

import random

MOVE = ['rock', 'paper', 'scissors']

while True:
    inputList = []
    check = True
    p2 = 'P2'
    #Get user inputs
    print(f'You are playing rock, paper, scissors')
    
    while check == True:
        botCheck = input('Would you like to play with the computer? [y/n]').lower()
        
        print()
        
        inputList.append(input('P1 turn. Rock, Paper, or Scissors?').lower())
        
        print()
        
        if botCheck == 'n':
            inputList.append(input(f'{p2} turn. Rock, Paper, or Scissors?').lower())
        else:
            p2 = 'Computer'
            print(f'{p2} turn. Rock, Paper, or Scissors?')
            inputList.append(random.choice(MOVE))

        for i in inputList:
            if not i in MOVE:
                print('Invalid Inputs')
                inputList = []
            else:
                check = False
    
    print()
    
    #Game logic
    if inputList[0] == inputList[1]:
        print('It\'s a Draw!')
    else:
        if inputList[0] == 'rock':
            if inputList[1] == 'paper':
                print('P2 Win!')
            else:
                print('P1 Win!')
        elif inputList[0] == 'paper':
            if inputList[1] == 'scissors':
                print('P2 Win!')
            else:
                print('P1 Win!')
        else:
            if inputList[1] == 'rock':
                print('P2 Win!')
            else:
                print('P1 Win!')
    
    if not botCheck == 'n':
        print(f'\nComputer chose {inputList[1]}')
                
    replay = input('\nReplay? [y/n]?').lower()
        
    if not replay == 'y':
        break
    print()