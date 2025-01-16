import sys

count = int(input())
scores = list(map(int, sys.stdin.readline().strip().split()))

max_score = max(scores)

adjusted_scores = [(score / max_score) * 100 for score in scores]
print(sum(adjusted_scores) / count)