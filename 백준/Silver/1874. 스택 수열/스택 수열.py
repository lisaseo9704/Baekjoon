n = int(input())
target_sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current_num = 1

for target in target_sequence:
    while current_num <= target:
        stack.append(current_num)
        result.append("+")
        current_num += 1
    
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

for op in result:
    print(op)