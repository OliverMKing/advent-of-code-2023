from typing import Set
import fileinput

NO_NUM = -1

schematic = [line.strip() for line in fileinput.input()]

def isSymbol(char: str) -> bool:
    if char.isdigit():
        return False
    
    if char == ".":
        return False
    
    return True

# construct set of coordinates of each symbol 
symbol_coords = set()
for y in range(len(schematic)):
    row = schematic[y]
    for x in range(len(row)):
        if isSymbol(schematic[y][x]):
            symbol_coords.add((x, y))

# construct set of each coordinate adjacent to each symbol
def adjacentCoords(coord: tuple[int]) -> Set[tuple[int]]:
    adj = set()
    for adder in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        adj.add((coord[0] + adder[0], coord[1] +  adder[1]))
    return adj

adjacent_coords = set()
for coord in symbol_coords:
    adjacent_coords |= adjacentCoords(coord)


# go through each line checking if numbers are in adjacent coords
total = 0
for y in range(len(schematic)):
    row = schematic[y]

    numStart = NO_NUM
    adjacent = False
    for x in range(len(row)):
        if row[x].isdigit():
            if numStart == NO_NUM:
                numStart = x
            if (x, y) in adjacent_coords:
                adjacent = True
        else:
            if numStart != NO_NUM and adjacent:
                total += int(row[numStart:x])

            numStart = NO_NUM
            adjacent = False
    
    if numStart != NO_NUM and adjacent:
        total += int(row[numStart:])

print(total)


