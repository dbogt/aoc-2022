# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:46:47 2022

@author: Bogdan Tudose
"""
#%% Source files
fPath = "../aoc-2022-Src/"
# f = open(fPath+"d4DemoInputs.txt", "r")
f = open(fPath+"d4ActualInputs.txt", "r")
inputs = f.read()
inputs = inputs.splitlines()
assignments = [ line.split(',') for line in inputs]
#%% Part 1
ranges = []
fullOverlapCounter = 0
someOverlap = 0 #counter for Part 2
for assignment in assignments:
    elf1 = [int(x) for x in assignment[0].split('-')]
    elf2 = [int(x) for x in assignment[1].split('-')]
    set1 = set([x for x in range(elf1[0],elf1[1]+1)])
    set2 = set([x for x in range(elf2[0],elf2[1]+1)])
    inters = set1 & set2
    if len(inters) == len(set1) or len(inters) == len(set2):
        fullOverlapCounter += 1        
    if len(inters) > 0: #code for Part 2
        someOverlap += 1
    ranges.append([set1, set2, inters])
print("Part 1:", fullOverlapCounter)

#%% Part 2
print("Part 2:", someOverlap)
