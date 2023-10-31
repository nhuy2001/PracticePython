#Huy Nguyen
#Date Created: 2023-10-30
#Last Updated: 2023-10-30

#Requirement: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

while True:
    try:
        sentence = input('Please Enter any Sentence of any Length: ').split()
    except:
        print('Invalid Input')
    else:
        print(f'Here\'s your input sentence: {sentence}')
        break

outputString = []

for i in reversed(sentence):
    outputString.append(i)

print()
print(f'Here\'s your sentence reversed: {outputString}')