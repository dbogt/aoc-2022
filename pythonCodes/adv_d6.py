# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:57:37 2022

@author: Bogdan Tudose
"""
#%% Source files
fPath = "../aoc-2022-Src/"
# f = open(fPath+"d6DemoInputs.txt", "r")
f = open(fPath+"d6ActualInputs.txt", "r")
inputs = f.read()
#Letters
letters = [l for l in inputs]

#%% Part 1
def findIndex(letters, distinct):
    for idx in range(distinct,len(letters)):
        setLetters = set(letters[idx-distinct:idx])
        if len(setLetters)==distinct:
            return idx

distinctPart1 = 4 
print("Part 1", findIndex(letters, distinctPart1))

#%% Part 2
distinctPart2 = 14 
print("Part 2", findIndex(letters, distinctPart2))

    