#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

#Requirement: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

import random

def listGen(long = 10, boundVal = 100, seedVal = 0):
    random.seed(seedVal) #Set seed
    outputList = random.sample(range(boundVal), long)
    
    return outputList

def rmDup(inputList):
    inputList = list(set(inputList))
    
    return inputList

rmDup(listGen())