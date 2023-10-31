#Huy Nguyen
#Date Created: 2023-10-23
#Last Updated: 2023-10-23

#Requirement: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

#Part 1:
while True:
    try:
        numInput = int(input(f'Please enter a number: '))
    except:
        print('The input was not a valid integer.\n')
    else:
        mod2 = numInput % 2
        mod4 = numInput % 4
        break
    
if mod2 == 0 and mod4 == 0:
    print('This even number is a multiple of 4!')
elif mod2 == 0 and mod4 != 0:
    print('This is an even number!')
elif mod2 == 1:
    print('This is an odd number!')

#Part 2:
while True:
    try:
        num1, num2 = input('\nFor the next step, please enter two numbers separated by a single space: ').split()
    except ValueError:
        print('Please enter two inputs.\n')
    else:
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print('The inputs was not a valid integer.\n')
        else:
            numVal = (num1 / num2) % 2
            break

if numVal == 0:
    print('This is an even number!')
else:
    print('This is an odd number!')

