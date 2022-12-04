with open('Day 4 Camp Cleanup DATA.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# FIRST ANSWER
sections = []
contained = 0

for x in lines:
    sections += [x.split(",")]

for x in sections:
    firstMinMax = x[0].split("-")
    firstMinMax = [int(x) for x in firstMinMax]
    secondMinMax = x[1].split("-")
    secondMinMax = [int(x) for x in secondMinMax]

    if (firstMinMax[0] <= secondMinMax[0] and firstMinMax[1] >= secondMinMax[1]) or (secondMinMax[0] <= firstMinMax[0] and secondMinMax[1] >= firstMinMax[1]):
        contained += 1

print(contained)

# SECOND ANSWER
overlap = 0
allSections = []

for x in sections:
    firstMinMax = x[0].split("-")
    firstMinMax = [int(x) for x in firstMinMax]
    secondMinMax = x[1].split("-")
    secondMinMax = [int(x) for x in secondMinMax]

    allSections.append([[x for x in range(firstMinMax[0], firstMinMax[-1] + 1)], [y for y in range(secondMinMax[0], secondMinMax[-1] + 1)]])

for x in allSections:
    for y in x[0]:
        if y in x[1]:
            overlap += 1
            break

print(overlap)