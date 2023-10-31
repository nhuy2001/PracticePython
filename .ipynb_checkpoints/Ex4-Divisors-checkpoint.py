#Huy Nguyen
#Date Created: 2023-10-24
#Last Updated: 2023-10-24

while True:
    try:
        numVal = int(input('Please Enter a Number: '))
    except ValueError:
        print('The input was not a valid integer.\n')
    else:
        break
    
outputList = []

aList = range(1, numVal + 1)

for i in aList:
    modulo = numVal % i
    if modulo == 0:
        outputList.append(i)

print(f'Here a list of number that is divisible by {numVal}: \n{outputList}')