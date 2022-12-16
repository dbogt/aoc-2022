# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:59:15 2022

@author: Bogdan Tudose
"""
#%% Source files
fPath = "../aoc-2022-Src/"
# f = open(fPath+"d5DemoInputs.txt", "r")
f = open(fPath+"d5ActualInputs.txt", "r")
inputs = f.read()

stacks = inputs.split('\n\n')[0]
moves = inputs.split('\n\n')[1]
moves = moves.splitlines()
stacks = stacks.splitlines()
stackNums = [int(x.strip()) for x in stacks[-1].split('  ')]
#%% Text Cleaning for both parts
cleanMoves = []
for move in moves:
    rules = move.replace('move','').replace('from','').replace('to','').strip()
    rules = rules.split('  ')
    countMoved = int(rules[0].strip())
    startStack = int(rules[1].strip())
    endStack = int(rules[-1].strip())
    cleanMoves.append([countMoved, startStack, endStack])
#%% Functins to create stacks and output top crates
def createStacks():
    stacksDict = {x:[] for x in stackNums}
    for row in stacks[:-1]:
        idx = 1
        for col in stackNums:
            if row[idx] != ' ':
                stacksDict[col].append(row[idx])
            idx += 4 #1, 5, 9, etc.
    return stacksDict

def outputTop(stacksDict):
    topCrates = ""
    for stack in stacksDict.values():
        topCrates += stack[0] 
    print(topCrates)

#%% Part 1 - Make Moves
stacksDict = createStacks()
for move in cleanMoves:
    numToMove = move[0]
    fromStack = move[1]
    toStack = move[-1]
    for crateNum in range(numToMove):
        crateLetter = stacksDict[fromStack][0]
        stacksDict[toStack].insert(0, crateLetter)
        stacksDict[fromStack].pop(0)

outputTop(stacksDict)
#%% Part 2
stacksDict = createStacks()
for move in cleanMoves:
    numToMove = move[0]
    fromStack = move[1]
    toStack = move[-1]
    cratesToMove = stacksDict[fromStack][0:numToMove]
    stacksDict[fromStack] = stacksDict[fromStack][numToMove:]
    stacksDict[toStack] = cratesToMove.copy() + stacksDict[toStack]
outputTop(stacksDict)
    


