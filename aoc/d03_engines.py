import sys
from typing import List
from itertools import takewhile

def get_parts(schematic: List):
    parts = []
    for y in range(len(schematic)):
        for x in range(len(schematic[0])):
            if schematic[y][x].isnumeric():
                num = list(takewhile(lambda i: i.isnumeric(), schematic[y][x:]))
                symbols= []
                n_pt = None
                for i in range(len(num)):
                    schematic[y][x+i]='.'
                    neighbours = [-1, 0, 1]
                    for h in neighbours:
                        if y+h < len(schematic):
                            for l in neighbours:
                                if x+i+l < len(schematic[0]):
                                    neighbour = schematic[y+h][x+i+l]
                                    if neighbour != '.' and not neighbour.isnumeric(): 
                                        symbols.append(neighbour)
                                        n_pt = (y+h, x+i+l)

                if len(symbols) > 0:
                    parts.append({ 'num': int(''.join(num)), 'pt': n_pt, 'sym': list(set(symbols))[0]})
    return parts

def main(input):
    schematic = []
    with open(input, mode="r") as file:
        schematic = [list(line.strip()) for line in file.readlines()]

    parts = get_parts(schematic)
    parts_total = 0
    for part in parts:
        parts_total += part['num']

    gear_ratios = {}
    for part in [part for part in parts if part['sym'] == '*']:
        g_sym = part['pt']
        nums = [part['num'] for part in parts if part['pt'] == g_sym]
        if len(nums) == 2 and not g_sym in gear_ratios:
            gear_ratios[g_sym] = nums[0]*nums[1]

    ratio_total = 0
    for k,v in gear_ratios.items():
        ratio_total += v


    return { 'parts': parts_total, 'ratio': ratio_total }


if __name__ == '__main__':
    print('Total: ', main(sys.argv[1]))
