import sys
from itertools import combinations

count, goal = map(int, input().split())
numbers = map(int, sys.stdin.read().strip().split())

b_sum = 0

for combo in combinations(numbers, 3):
    card_sum = sum(combo)
    if card_sum <= goal:
        b_sum = max(b_sum, card_sum)

print(b_sum)