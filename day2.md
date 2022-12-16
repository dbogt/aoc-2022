## [AOC2022-D02] Day 2: Rock Paper Scissors
- I used a lot of python dictionaries for this one, there is probably a more efficient way of doing it but I went for readability of code over conciseness
- not much more to it aside from mapping out all the coded letters properly with rock/papers/scissors and the outcome scores
https://adventofcode.com/2022/day/2

<details>
  <summary>Part 1 Solution</summary>
  
  I wanted to get clever with my list comprehension, but kept it relatively simple and just did a normal for loop at one point for Part 1.
  Part 2 was pretty easy with just doing a quick .sort (built-in list method) and then slicing on the last 3 numbers.

  ```python
  #%% Source files
  fPath = "../aoc-2022-Src/"
  # f = open(fPath+"d2DemoInputs.txt", "r")
  f = open(fPath+"d2ActualInputs.txt", "r")
  inputs = f.read()

  inputs = inputs.splitlines()
  rounds = [line.split(' ') for line in inputs]
  #%% Part 1

  # Maps
  # A = rock, B = paper, C= scissors
  # X = rock, Y = paper, Z=scissors

  scoreShapes = {'X':1, 'Y':2, 'Z':3}
  scoreOutcome = {'win':6, 'lose':0, 'draw':3}

  outcomes = {'A':{'X':'draw','Y':'win','Z':'lose'},
              'B':{'X':'lose','Y':'draw','Z':'win'},
              'C':{'X':'win','Y':'lose','Z':'draw'}}

  # Rounds
  scores = []
  for game in rounds:
      pick1 = game[0] #A, B or C
      pick2 = game[1] #X, Y or Z
      outcome = outcomes[pick1][pick2]
      totalScore = scoreShapes[pick2] + scoreOutcome[outcome]
      scores.append(totalScore)

  print("Part 1:",sum(scores))
  ```
</details>

<details>
  <summary>Part 2 Solution</summary>
    
  ```python
  #%% Part 2
  scoreShapes = {'A':1, 'B':2, 'C':3}
  scoreOutcome = {'win':6, 'lose':0, 'draw':3}
  rules = {'X':'lose', 'Y':'draw', 'Z':'win'}
  outcomes = {'A':{'win':'B','lose':'C','draw':'A'},
              'B':{'win':'C','lose':'A','draw':'B'},
              'C':{'win':'A','lose':'B','draw':'C'}}

  scores = []
  for game in rounds:
      # game = rounds[0]
      pick1 = game[0] #A, B or C
      rule = game[1] #X, Y or Z
      outcome = rules[rule]
      pick2 = outcomes[pick1][outcome]
      totalScore = scoreShapes[pick2] + scoreOutcome[outcome]
      scores.append(totalScore)
    
  print("Part 2:",sum(scores))
  ```
</details>

<details>
  <summary>Part 2 "Clever" Solution</summary>
  
  Here's part 2 with less dictionaries/mapping, just storing all the options in a list, but not a big fan of trying to get clever with the index numbers. I think I still prefer my first solution, was easier to code out and also read what I was trying to do.
  
  ```python
  #%% Part 2 more efficient
  picks = ['A','B','C']
  scoreOutcome = {'Z':6, 'X':0, 'Y':3}
  scoreShapes = {'A':1, 'B':2, 'C':3}

  scores = []
  #x = lose, y = draw, z = win
  for game in rounds:
      pick1 = game[0] #A, B or C
      rule = game[1] #X, Y or Z
      if rule == 'Y': #draw
          pick2 = pick1
      elif rule == 'Z': #win
          pick2 = picks[picks.index(pick1) - 3 + 1]
      else: #lose
         pick2 = picks[picks.index(pick1) - 1]
      totalScore = scoreShapes[pick2] + scoreOutcome[rule]
      scores.append(totalScore)    

  print("Part 2:",sum(scores))
  ```
</details
