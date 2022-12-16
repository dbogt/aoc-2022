## [AOC2022-D04] Day 4: Camp Cleanup
- Another day of using sets in Python and the intersection method used for yesterday's solve came in handy today (again can also use `set1 & set2`)
- Part 2 was super fast if you've set up part 1 with sets as well (only added 2 more lines of code to my part 1 to solve part 2)

https://adventofcode.com/2022/day/4

<details>
  <summary>Part 1 & 2 Solution</summary>
  
  My full approach to solving it:
  - text cleanup: split the lines, split each line on the comma, then split each "elf" on the dash
  - I created quick sets for each elf of their assignments (x for x in range(lowend, topend)) where lowend was the first number in x-y of assignments, and topend is the last number in that range
  - did the same for both elves, then just did a quick set1 & set2 to find which assignments overlap in each pair of elves
  - if the length of the overlap is = to the length of either elf's assignments then one must be overlapped fully in the other, and I increase my counter by one
  - for part 2, just made another counting variable where I check if the length of overlapped set is > 0
  
  ```python
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
  
  ```
</details>
