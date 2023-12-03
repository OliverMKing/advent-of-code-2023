import fileinput
from collections import defaultdict

END_WORD_KEY = "END"

# construct a trie to efficiently check if letters are numbers
words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
recursive_dict=  lambda: defaultdict(recursive_dict)
trie = recursive_dict()
for word, val in words.items():
    last = trie
    for letter in word:
        last = last[letter]
    last[END_WORD_KEY] = val

total = 0


def getNumber(line: str, i: int) -> int | None:
    if line[i].isdigit():
        return int(line[i])

    currTrie = trie
    while currTrie[line[i]]:
        currTrie = currTrie[line[i]]
        if END_WORD_KEY in currTrie:

            return currTrie[END_WORD_KEY]
        
        i += 1
        if i >= len(line):
            break

    return None


for line in fileinput.input():
    # use left and right pointer that move inwards to find first number on each side
    l, r = 0, len(line) - 1

    lNum = 0 
    while not (lNum := getNumber(line, l)):
        l += 1
    total += lNum * 10
    

    rNum = 0
    while not (rNum := getNumber(line, r)):
        r -= 1
    total += rNum

    print(lNum, rNum)

print(total)