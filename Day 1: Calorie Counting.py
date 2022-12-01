with open('2022-12-01.txt') as f:
    lines = f.readlines()

previousChar = ""
elfNumber = 0
elvesCalories = [[]]

for x in lines:
    if x == "\n":
        elfNumber += 1
        elvesCalories += [[]]
    elif x != "\n":
        elvesCalories[elfNumber] += [int(x)]

totElvesCalories = [sum(x) for x in elvesCalories]

# FIRST ANSWER
mostCalories = 0

for x in totElvesCalories:
    if x > mostCalories:
        mostCalories = x

print(mostCalories)

# SECOND ANSWER
firstCalories = 0
secondCalories = 0
thirdCalories = 0

for x in totElvesCalories:
    if x >= firstCalories:
        thirdCalories = secondCalories
        secondCalories = firstCalories
        firstCalories = x
    elif x >= secondCalories:
        thirdCalories = secondCalories
        secondCalories = x
    elif x >= thirdCalories:
        thirdCalories = x

totalCaloriesTop3 = sum([firstCalories, secondCalories, thirdCalories])

print(totalCaloriesTop3) # 2nd answer
