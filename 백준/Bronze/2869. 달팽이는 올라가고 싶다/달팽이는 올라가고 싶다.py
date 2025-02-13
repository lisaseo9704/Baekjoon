import math

def snail(a, b, v):
    days = math.ceil((v - a) / (a - b))
    return days + 1

def main():
    a, b, v = map(int, input().split())
    print(snail(a, b, v))

if __name__ == '__main__':
    main()
