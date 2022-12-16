# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 00:23:29 2022

@author: Bogdan Tudose
"""
#%% Source files
fPath = "../aoc-2022-Src/"
# f = open(fPath+"d3DemoInputs.txt", "r")
f = open(fPath+"d3ActualInputs.txt", "r")
inputs = f.read()
inputs = inputs.splitlines()

#%% Part 1
allCommon = []
# ord('a') #97; needs to be 1, so -96
# ord('z') #122; needs t be 26, so -96
# ord('A') #65; needs to be 27, so -38
# ord('Z') #90; -38
for rucksack in inputs:    
    half = int(len(rucksack) / 2)
    compart1 = rucksack[:half]
    compart2 = rucksack[half:]

    unique1 = set([x for x in compart1])
    unique2 = set([x for x in compart2])
    common = [x for x in unique1 if x in unique2]
    allCommon.append(common[0])

priorities = [ord(letter)-38 if letter.isupper() else ord(letter)-96 for letter in allCommon ]
print("Part 1:", sum(priorities))    

#%% Part 2
import pandas as pd
badges=[]
totalGroups = int(len(inputs)/3)

for groupNum in range(1, totalGroups + 1):
    start = groupNum * 3 - 3
    end = groupNum * 3
    rucksacks = inputs[start:end]
    uniqueSets = [set([item for item in items]) for items in rucksacks]
    allUnique = []
    for rucksack in uniqueSets:
        allUnique.extend(rucksack)
    df = pd.DataFrame({'Item':allUnique})
    counts = pd.DataFrame(df['Item'].value_counts())
    badge = counts[counts['Item']==3].index[0]
    badges.append(badge)

priorities = [ord(letter)-38 if letter.isupper() else ord(letter)-96 for letter in badges]
print("Part 2:", sum(priorities))    
