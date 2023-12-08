from pprint import pprint
import sys

def get_almanac(fname):
    with open(fname, mode="r") as file:
        return file.read()
    
def translate_value(value, map):
    found = False
    for (dest, start, range) in map:
        if value >= start and value <= (start + range):
            found = True
            return dest + (value - start)
        
    if not found:
        return value
        

def main(input):
    almanac = get_almanac(input).split('\n\n')
    seeds = [int(seed) for seed in almanac[0].split()[1:]]

    maps = []
    for map in almanac[1:]:
        temp = [int(v) for v in map.split(':\n')[-1].split()]
        temp_it = iter(temp)
        maps.append(list(zip(temp_it, temp_it, temp_it)))

    part1_ends = []
    for seed in seeds:
        val = seed
        for map in maps:
            val = translate_value(val, map)
        part1_ends.append(val)

    part2_ends = []
    expanded_seeds = []
    for [start, rng] in (seeds[pos:pos + 2] for pos in range(0, len(seeds), 2)):
        expanded_seeds += [start + i for i in range(rng)]

    for seed in expanded_seeds:
        val = seed
        for map in maps:
            val = translate_value(val, map)
        part2_ends.append(val)

    return {'part1': min(part1_ends), 'part2': min(part2_ends) }

if __name__ == '__main__':
    print('Total: ', main(sys.argv[1]))