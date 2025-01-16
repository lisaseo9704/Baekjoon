import math

part = int(input())
t_size = list(map(int, input().split()))
t, p = map(int, input().split())

t_shirt = [math.ceil(i/t) for i in t_size]
print(sum(t_shirt))
print(part//p, part%p)