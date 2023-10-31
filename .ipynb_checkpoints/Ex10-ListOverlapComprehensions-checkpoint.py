#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

import random

random.seed(0)

a = random.sample(range(100), 25)
b = random.sample(range(100), 35)

print([i for i in a if i in b])