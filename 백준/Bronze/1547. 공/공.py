num = int(input())

ball = [0]*4
ball[1] = 1

for _ in range(num):
    a,b = map(int, input().split())
    tmp = ball[a]
    ball[a] = ball[b]
    ball[b] = tmp

print(ball.index(1))