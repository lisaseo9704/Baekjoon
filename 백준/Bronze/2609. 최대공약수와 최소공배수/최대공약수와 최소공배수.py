import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

m,n = map(int, input().split())
sys.stdout.write(f'{gcd(m,n)}\n{lcm(m,n)}')