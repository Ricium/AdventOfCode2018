from AdventOfCode2018 import *

def part_one(data):
    value = 0
    for x in data:
        value += x
    return value

def part_two(data):
    value = 0
    frequencies = []
    frequencies.append(value)
    found = False
    while True:
        for x in data:
            value += x
            if value in frequencies:
                found = True
                break
            else:
                frequencies.append(value)   
        if found:
            break
    return value  
    
x = functions()
data = x.read_integers("input/day1_input.txt")
print('Part One: ' + str(part_one(data)))
print('Part Two: ' + str(part_two(data)))

