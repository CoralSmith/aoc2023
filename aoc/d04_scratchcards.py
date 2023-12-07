from dataclasses import dataclass
import sys
from typing import List, Set

@dataclass
class Card:
    win_nums: Set[int]
    res_nums: Set[int]

def parse_card(card_str: str):
    l = card_str.split(': ')
    [win_str, res_str] = l[-1].split(' | ')
    return Card(set([int(n) for n in win_str.split()]), set([int(n) for n in res_str.split()]))

def main(input):
    scores = []
    matches = []
    with open(input, mode="r") as file:
        for line in (line.strip() for line in file.readlines()):
            item = parse_card(line)
            winning_nums = list(item.win_nums.intersection(item.res_nums))
            score = 0 if len(winning_nums) == 0 else (1 if len(winning_nums) == 1 else 2**(len(winning_nums)-1))
            scores.append(score)
            matches.append(len(winning_nums))


    hand = [{'qty': 1, 'qual': match} for match in matches]
    for idx, item in enumerate(hand):
        if item['qty'] > 0:
            for card in hand[idx+1:idx+1+item['qual']]:
                card['qty'] += item['qty']


    return { 'score': sum(scores), 'quantity': sum([item['qty'] for item in hand]) }



if __name__ == '__main__':
    print('Total: ', main(sys.argv[1]))