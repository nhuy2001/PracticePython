#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

#Requirement: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

random.seed(0)

a = random.sample(range(100), 25)
b = random.sample(range(100), 35)

print([i for i in a if i in b])