#Huy Nguyen
#Date Created: 2023-10-24
#Last Updated: 2023-10-24

while True:
    try:
        seedVal, len1, len2 = input(f'Please Enter Three Numbers:\n-First number for the seed.\n-Second number for the length of the first list.\n-Third number for the length of second list.\n').split()
    except ValueError:
        print('Please enter three inputs.\n')
    else:
        try:
            seedVal = int(seedVal)
            len1 = int(len1)
            len2 = int(len2)
        except ValueError:
            print('The inputs was not a valid integer.\n')
        else:
            break

import random
random.seed(seedVal)

START_VAL = 1
END_VAL = 100
    
a = [ int(random.randint(START_VAL, END_VAL)) for i in range(len1) ]
b = [ int(random.randint(START_VAL, END_VAL)) for i in range(len2) ]


outputList = []

for i in set(a):
    if i in set(b):
        outputList.append(i)

print()
print(f'Here\'s your first list:\n{a}\n')
print(f'Here\'s your second list:\n{b}\n')
print(f'Here\'s a list of common variables:\n{outputList}')