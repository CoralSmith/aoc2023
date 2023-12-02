import sys
from itertools import groupby
from typing import Dict, List

def parse_input(input):
    games = []
    with open(input, mode="r") as file:
        res=[]
        for line in (line.strip() for line in file.readlines()):
            mid = line.replace('Game ', '').replace(':',' game,').replace(';', ',')
            res.append([r.split() for r in mid.split(', ')])
        
        for game in res:
            game.sort(key=lambda x: x[1])
            games.append({k: [int(x) for x,y in g] for k,g in groupby(game,key=lambda x: x[1])})
    return games

def all_possible(target: Dict[str, List[int]], input):
    return all([all(r <= v for r in input[k]) for k, v in target.items()])

def possible(input):
    target = {'red': 12, 'green': 13, 'blue':14}
    possible = [p for p in filter(lambda x: all_possible(target, x), input)]
    return sum([g['game'][0] for g in possible])

def power(input):
    mins = [{k: max(v) for k,v in game.items()} for game in input]
    return sum([g['red']*g['green']*g['blue'] for g in mins])

def main(input):
    games = parse_input(input)

    return { 'possible': possible(games), 'power': power(games) }

if __name__ == '__main__':
    print('Total: ', main(sys.argv[1]))