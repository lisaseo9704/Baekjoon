def count_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def main():
    n = int(input())
    print(count_zeros(n))

if __name__ == '__main__':
    main()