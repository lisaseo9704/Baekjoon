import sys
num_list = []
for line in sys.stdin:
    num_list.append(int(line))

max_num = max(num_list)
print(max_num)
print(num_list.index(max_num)+1)