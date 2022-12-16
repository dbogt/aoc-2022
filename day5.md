## [AOC2022-D05] Day 5: Supply Stacks
- a lot of dictionary and lists manipulation for this one
- took a bit longer than I expected to clean up the text at beginning and grab the individual letters to create the stacks
- once that was done, it was list manipulation to move the letters/crates around in the lists
- helpful hint for lists: use `listName.pop(index)` to remove a specific "row", and `listName.inset(index, value)` to insert the value in a specific row
- for part two, you can slice a list (e.g. `listName[x:y]`) and also merge two lists by adding them, for example ['a', 'b', 'c'] + ['x', 'y', 'z'] creates ['a', 'b', 'c', 'x', 'y', 'z'] 

https://adventofcode.com/2022/day/5

<details>
  <summary>Code to clean up data (both parts)</summary>
  
  Code common for both parts:
  - importing data
  - doing some text manipulation to break apart the moves/rules at bottom of text from the crates info at top
  
  ```python
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
  ```
  
  Also made some functions to quickly re-create the initial stacks for both part one and two and create final output of the top crates:
  ```python
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
  ```
</details>

<details>
  <summary>Part 1 Solution</summary>
    
  And here is solution for Part 1 - where we're moving the crates one box/letter at a time:
  ```python
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
  ```
</details>

<details>
  <summary>Part 2 Solution</summary>
    
  And Part 2 - where we're moving multiple crates at a time:
  ```python
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
  ```
</details>
