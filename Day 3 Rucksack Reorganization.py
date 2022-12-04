import string
from itertools import zip_longest

with open('Day 3 Rucksack Reorganization DATA.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# FIRST ANSWER
alphabetValue = {}
correspondentValue = 1
lowerAlphabet = list(string.ascii_lowercase)
upperAlphabet = list(string.ascii_uppercase)

for x in lowerAlphabet + upperAlphabet:
    alphabetValue[x] = correspondentValue
    correspondentValue += 1

allDuplicates = []
prioritiesSum = 0

for x in lines:
    firstCompartment = x[:len(x) // 2]
    secondCompartment = x[len(x) // 2:]
    duplicates = []

    for x in firstCompartment:
        if x in secondCompartment:
            duplicates += [x]
    
    allDuplicates += list(set(duplicates))

for x in allDuplicates:
    prioritiesSum += alphabetValue[x]

print(prioritiesSum)

# SECOND ANSWER
groupedRucksack = []
groupsLetters = []
prioritiesSum = 0

for x in range(1, len(lines)):
    if x % 3 == 0:
        groupedRucksack += [lines[x - 3:x]]

for x in groupedRucksack:
    for z in x[0]:
        if z in x[1] and z in x[2]:
            groupsLetters += [z]
            #print(z, x)
            break

for x in groupsLetters:
    prioritiesSum += alphabetValue[x]

print(prioritiesSum)

letters = string.ascii_letters
prioritiesSum = 0
groups = list(zip_longest(*[iter(lines)]*3, fillvalue=''))

for (a, b, c) in groups:
    prioritiesSum += letters.index([x for x in a if x in b and x in c][0]) + 1

print(prioritiesSum)