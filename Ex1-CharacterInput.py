#Huy Nguyen
#Date Created: 2023-10-23
#Last Updated: 2023-10-23

#Requirements: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

name = input('What\'s your name? ')
print(f'Your name is {name}')
print()

while True:
    try:
        age = int(input('What\'s your current age? '))
    except ValueError:
        print('The input was not a valid integer.\n')
    else:
        print(f'Your age is {age}')
        break

print()

CURRENT_YEAR = int(datetime.date.today().strftime('%Y'))

YEAR_100 = CURRENT_YEAR - age + 100

print(f'You\'ll be 100 years old in {YEAR_100}')

while True:
    try:
        count = int(input('How many times would you like to repeat the above message? '))
    except ValueError:
        print('The input was not a valid integer.\n')
    else:
        break

i = 0

while i < count:
    print(f'You\'ll be 100 years old in {YEAR_100}')
    i += 1