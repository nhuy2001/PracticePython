#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

def getFibo(num):
    startList = [0, 1]
    i = 1
    while i <= num:
        startList.append(startList[-1] + startList[len(startList) - 2])
        i += 1
    return print(f'Here\'s Your Fibonnaci List: \n{startList}')

while True:
    try:
        numVal = int(input('Enter the Desire Length of the Fibonnaci Sequence: '))
    except:
        print('Invalid Input')
    else:
        break

print()
getFibo(numVal)