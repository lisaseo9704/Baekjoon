def is_valid_ps(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    ps = input()
    print(is_valid_ps(ps))