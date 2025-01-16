m,n = map(int, input().split())
if m > m-n:
    n = m-n
bunja = 1
bunmo = 1

for i in range(1, n+1):
    bunja *= (m-i+1)
    bunmo *= i

print(bunja // bunmo)