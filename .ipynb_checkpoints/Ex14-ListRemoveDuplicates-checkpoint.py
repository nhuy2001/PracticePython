#Huy Nguyen
#Date Created: 2023-10-26
#Last Updated: 2023-10-26

import random

def listGen(long = 10, boundVal = 100, seedVal = 0):
    random.seed(seedVal) #Set seed
    outputList = random.sample(range(boundVal), long)
    
    return outputList

def rmDup(inputList):
    inputList = list(set(inputList))
    
    return inputList

rmDup(listGen())