import fileinput

total = 0

for line in fileinput.input():
    # use left and right pointer that move inwards to find first number on each side
    l, r = 0, len(line) - 1

    while not line[l].isdigit():
        l += 1
    total += int(line[l]) * 10
    

    while not line[r].isdigit():
        r -= 1
    total += int(line[r])


print(total)