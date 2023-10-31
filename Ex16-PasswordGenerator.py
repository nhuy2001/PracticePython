#Huy Nguyen
#Date Created: 2023-10-30
#Last Updated: 2023-10-30

#Requirement: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

from english_words import get_english_words_set
import random
import string

passStr = ['weak', 'medium', 'strong']
web2_lower = list(get_english_words_set(['web2'], lower=True)) #Web2 dictionary, converted to lowercase

#Lists of all characters
lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
number = list(string.digits)
specialChar = list(set(string.punctuation))

MAX_LENGTH = 25
STR_MIN_LENGTH = 14
MID_MIN_LENGTH = 6

#-------------------------------------------------------------------------------------------------------

def strongPassword ():
    passLen = random.choice(range(STR_MIN_LENGTH, MAX_LENGTH))
    
    outputString = ''
    
    order = [lowerCase, upperCase, number, specialChar]
    
    listLength = len(order)

    for i in range(1, passLen + 1):
        currentItem = random.choice(order)
        randIndex = random.choice(range(0, len(currentItem)))
        outputString += currentItem[randIndex]
        
    return print(f'Your password is: \n{outputString}\n\nPassword Length: {passLen}')

#-------------------------------------------------------------------------------------------------------
    
def mediumPassword ():
    choice = random.choice([1, 2])
    outputString = ''
    
    if choice == 1:
        passLen = random.choice(range(MID_MIN_LENGTH, STR_MIN_LENGTH))
        
        order = [lowerCase, upperCase, number, specialChar]
        
        listLength = len(order)

        for i in range(1, passLen + 1):
            currentItem = random.choice(order)
            randIndex = random.choice(range(0, len(currentItem)))
            outputString += currentItem[randIndex]
            
        return print(f'Your password is: \n{outputString}\n\nPassword Length: {passLen}')
        
    else:
        passLen = random.choice(range(STR_MIN_LENGTH, MAX_LENGTH))
        
        order = [lowerCase, upperCase, number]
        
        listLength = len(order)

        for i in range(1, passLen + 1):
            currentItem = random.choice(order)
            randIndex = random.choice(range(0, len(currentItem)))
            outputString += currentItem[randIndex]
            
        return print(f'Your password is: \n{outputString}\n\nPassword Length: {passLen}')

#-------------------------------------------------------------------------------------------------------
 
def weakPassword ():
    easyPass = random.choice(web2_lower)
    
    return print(f'Your password is: {easyPass}\n\nPassword Length: {len(easyPass)}')
    
#-------------------------------------------------------------------------------------------------------

while True:
    check = True
    while check == True:
        inputVal = input('How Strong Would You Like Your Password to be? [weak/medium/strong]\n').lower()
        if not inputVal in passStr:
            print('\nInvalid input')
        else:
            check = False
            break
    print()

    if inputVal == 'strong':
        strongPassword()
    elif inputVal == 'medium':
        mediumPassword()
    else:
        weakPassword()
    
    print()
    while True:
        contChoice = input('Would You Like to Generate Another Password? [y/n]').lower()
        if not contChoice in ['y', 'n']: 
            print('\nInvalid Input!\n')
        else:
            break
    print()
    
    if contChoice == 'n':
        break