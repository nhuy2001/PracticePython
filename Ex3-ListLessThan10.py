#Huy Nguyen
#Date Created: 2023-10-23
#Last Updated: 2023-10-23

#Requirement: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

while True:
    try:
        myList = list(map(int, input('Please enter as many numbers as you like: ').split()))
    except ValueError:
            print('The inputs was not a valid integer.\n')
    else:
        break

newList = []
        
for i in myList:
    if i < 5:
        newList.append(i)

print(f'\nHere\'s your new list of numbers less than 5:\n{newList}')

print()

while True:
    try:
        numVal = int(input('Please enter a number: '))
    except ValueError:
            print('The inputs was not a valid integer.\n')
    else:
        break

newList2 = []

for i in myList:
    if i < numVal:
        newList2.append(i)
        
print(f'\nHere\'s your new list of item less than {numVal}:\n{newList2}')

