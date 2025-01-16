import sys
input = sys.stdin.read
data = input().split()

for number in data:
    if number == '0':
        break
    if number == number[::-1]:
        print('yes')
    else:
        print('no')