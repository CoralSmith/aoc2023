import sys

alternatives = {'one':'1', 'two':'2', 'three':'3', 'four': '4', 'five': '5', 'six': '6', 'seven':'7', 'eight':'8', 'nine': '9'}

total = 0

for line in (line.strip() for line in open(sys.argv[1], 'r').readlines()):
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

print('Total: ', total)