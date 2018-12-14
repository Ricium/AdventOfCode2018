from AdventOfCode2018 import *

def part_one(data):
    twoCount = 0
    threeCount = 0
    for word in data:
        occurances = x.countOccurance(word)
        if 2 in occurances:
            twoCount += 1
        if 3 in occurances:
            threeCount += 1
    return twoCount * threeCount

def part_two(data):
    data.sort()
    for i in range(len(data) - 1):
        for j in range(1, len(data)):
            comp, word = x.compare(data[i], data[j])
            if comp == 1:
                return ''.join(word)
    
x = functions()
data = x.read("input/day2_input.txt", "\n")

print('Part One: ' + str(part_one(data)))
print('Part Two: ' + str(part_two(data)))