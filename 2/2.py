import fileinput
from typing import List, Mapping
from dataclasses import dataclass

ALLOWED_RED = 12
ALLOWED_GREEN = 13
ALLOWED_BLUE = 14

@dataclass
class Game:
    id: int
    rounds: List[Mapping[str, int]]

def parseLine(line: str) -> Game:
    game_info, draws = line.split(": ")
    _, id = game_info.split(" ")
    rounds = draws.split("; ")
    mapped_rounds = [{color[1]: int(color[0]) for color in map(lambda x: x.split(" "), round.split(", "))} for round in rounds]

    return Game(int(id), mapped_rounds)

total = 0
for line in fileinput.input():
    game = parseLine(line.strip())

    red = 0
    green = 0
    blue = 0
    for round in game.rounds:
        if "red" in round:
            red = max(red, round["red"])
        if "green" in round:
            green = max(green, round["green"])
        if "blue" in round:
            blue = max(blue, round["blue"])

    total += red * green * blue

print(total)