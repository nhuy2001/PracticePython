#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

import random

random.seed(0)

sampleList = random.sample(range(100), 10)

outputList = [sampleList[0], sampleList[-1]]

print(f'Sample List: \n{sampleList}\n')
print(f'Output List: \n{outputList}')
