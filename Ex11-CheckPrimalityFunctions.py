#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

#Requirement: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

def checkPrime(numVal):
    if numVal % 2 == 0:
        return 'Input is a prime number!'
    else:
        return 'Input is not a prime number!'

while True:
    try:
        inputVal = int(input('Please Enter a Number: '))
    except:
        print('Invalid Input')
    else:
        break
    
checkPrime(inputVal)