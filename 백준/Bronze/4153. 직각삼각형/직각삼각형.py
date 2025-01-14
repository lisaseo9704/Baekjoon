import sys

for line in sys.stdin:
    line_list = list(map(int, list(line.split())))
    line_list.sort()
    if sum(line_list) == 0: break
    if (line_list[2]**2) == (line_list[0]**2) + (line_list[1]**2):
        print('right')
    else:
        print('wrong')