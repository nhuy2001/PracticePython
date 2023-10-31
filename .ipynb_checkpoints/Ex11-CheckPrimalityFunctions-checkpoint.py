#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

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