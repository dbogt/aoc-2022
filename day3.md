## [AOC2022-D03] Day 3: Rucksack Reorganization
- A bit of text manipulation again for this one, you can loop through a string and create a list of letters (e.g. `[x for x in 'gddfsljlasd']` will create a list of individual letters)
- Python has a data type called set, which gives you a unique list of values in a list, so `set(['a', 'a', 'c', 'd', 'c', 'A', 'A'])` will give you `{'a', 'c', 'd', 'A'}`
- you can find intersection of 2 sets (i.e. overlapping letters) with `set1.intersection(set2)` or shorthand `set1 & set2`
- Aside from that, got a bit lazy in part 2 and you can use Pandas built in method .value_counts() to quickly do a pivot of counts
- One last hint for both parts, ord(letter) in Python gives a numerical vale (e.g. ord('a') = 97, and ord('z')=122, can use that to figure out priorities a bit faster)

https://adventofcode.com/2022/day/3

<details>
  <summary>Part 1 Solution</summary>
  
  ```python
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
  ```
</details>

<details>
  <summary>Part 2 Solution</summary>
    
  ```python
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
  ```
</details>
