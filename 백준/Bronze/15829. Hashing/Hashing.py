import sys

L = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()

r = 31
M = 1234567891

hash_value = 0
for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1
    # pow(r, i, M)
    r_power = 1
    for j in range(i):
        r_power = (r_power * r) % M
    hash_value = (hash_value + (char_value * r_power) % M) % M

print(hash_value)