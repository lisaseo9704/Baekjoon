num = int(input())
num_line = input().split(' ')
num_list = list(map(int, num_line))
print(f'{min(num_list)} {max(num_list)}')