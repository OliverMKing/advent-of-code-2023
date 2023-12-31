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
    ok = True
    for round in game.rounds:
        if "red" in round and round["red"] > ALLOWED_RED:
            ok = False
        if "green" in round and round["green"] > ALLOWED_GREEN:
            ok = False
        if "blue" in round and round["blue"] > ALLOWED_BLUE:
            ok = False

    if ok:
        total += game.id

print(total)