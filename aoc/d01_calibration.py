import sys


def main(input):
    alternatives = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    total = 0

    with open(input, mode="r") as file:
        for line in (line.strip() for line in file.readlines()):
            nums = ''
            for i in range(len(line)):
                if line[i].isnumeric():
                    nums += line[i]
                else:
                    for k,v in alternatives.items():
                        if line[i:].startswith(k):
                            nums += v
            

            line_num = nums[0] + nums [-1]
            total += int(line_num)

    return total

if __name__ == '__main__':
    print('Total: ', main(sys.argv[1]))