# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 01:00:43 2021

@author: Bogdan Tudose
"""
#%% Source files
import numpy as np
fPath = "../aoc-2022-Src/"
# f = open(fPath+"d1DemoInputs.txt", "r")
f = open(fPath+"d1ActualInputs.txt", "r")
inputs = f.read()

#%% Part 1 Clever
calories = [[int(x) for x in  elf.splitlines()] for elf in inputs.split('\n\n')]
totalCals = [np.sum(cals) for cals in calories]
maxCals = np.max(totalCals)
print("Max calories:", maxCals)

#%% Part 1
elves = inputs.split('\n\n')
elves = [elf.splitlines() for elf in elves]

calories = []
for elf in elves:
    cals = [int(cal) for cal in elf]
    calories.append(cals)
        
totalCals = [np.sum(cals) for cals in calories]
maxCals = np.max(totalCals)
print("Max calories:", maxCals)

#%% Part 2
totalCals.sort()
print(totalCals[-3:], "Sum top 3", np.sum(totalCals[-3:]))

#%% Part 2 Pandas
import pandas as pd
df = pd.DataFrame({"Total Calories":totalCals})
df['Total Calories'].nlargest(3).sum()
