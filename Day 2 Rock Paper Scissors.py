with open('Day 2 Rock Paper Scissors DATA.txt') as f:
    lines = f.readlines()

# FIRST ANSWER
totalPoints = 0

for x in range(len(lines)):
    elfMove = lines[x][:1]
    myMove = lines[x][2:3]

    if elfMove == "A": # rock
        if myMove == "X": # rock
            totalPoints += 1 + 3
        elif myMove == "Y": # paper
            totalPoints += 2 + 6
        elif myMove == "Z": # scissors
            totalPoints += 3 + 0
    elif elfMove == "B": # paper
        if myMove == "X": # rock
            totalPoints += 1 + 0
        elif myMove == "Y": # paper
            totalPoints += 2 + 3
        elif myMove == "Z": # scissors
            totalPoints += 3 + 6
    elif elfMove == "C": # scissors
        if myMove == "X": # rock
            totalPoints += 1 + 6
        elif myMove == "Y": # paper
            totalPoints += 2 + 0
        elif myMove == "Z": # scissors
            totalPoints += 3 + 3

print(totalPoints)

# SECOND ANSWER
totalPoints = 0

for x in range(len(lines)):
    elfMove = lines[x][:1]
    myMove = lines[x][2:3]

    if elfMove == "A": # rock
        if myMove == "X": # lose
            totalPoints += 3 + 0
        elif myMove == "Y": # draw
            totalPoints += 1 + 3
        elif myMove == "Z": # win
            totalPoints += 2 + 6
    elif elfMove == "B": # paper
        if myMove == "X": # lose
            totalPoints += 1 + 0
        elif myMove == "Y": # draw
            totalPoints += 2 + 3
        elif myMove == "Z": # win
            totalPoints += 3 + 6
    elif elfMove == "C": # scissors
        if myMove == "X": # lose
            totalPoints += 2 + 0
        elif myMove == "Y": # draw
            totalPoints += 3 + 3
        elif myMove == "Z": # win
            totalPoints += 1 + 6

print(totalPoints)