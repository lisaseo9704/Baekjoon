import sys
input = sys.stdin.readline

def operation_only_command(S_set, command):
    if command == 'all':
        S_set.clear()
        S_set.update(range(1,21))
    elif command == 'empty':
        S_set.clear()

def operation(S_set, command, num):
    if command == 'add':
        S_set.add(num)
    elif command =='remove':
        S_set.discard(num)
    elif command == 'toggle':
        if num in S_set:
            S_set.remove(num)
        else:
            S_set.add(num)
    elif command == 'check':
        sys.stdout.write('1\n' if num in S_set else '0\n')

S_set = set()

for _ in range(int(input())):
    line = input().strip()
    if line == 'all' or line=='empty':
        operation_only_command(S_set, line)
    else:
        command, num = line.split()
        operation(S_set, command, int(num))