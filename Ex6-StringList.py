#Huy Nguyen
#Date Created: 2023-10-24
#Last Updated: 2023-10-24

#Requirement: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

while True:
    inputString = input('Please enter a word of any length: ')
    if not inputString.isalpha():
        print('The input was not a valid word.\n')
    else:
        break

outputList = []

for i in reversed(inputString):
    outputList.append(i)
    
reversedString = ''.join(outputList)

if inputString == reversedString:
    print(f'This word is a palindrome!')
else:
    print(f' This word is not a palindrome!')