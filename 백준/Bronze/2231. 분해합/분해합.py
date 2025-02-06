def get_decomposition_sum(n):
    return n + sum(map(int, str(n)))

def find_constructor(n):
    for i in range(1, n + 1):
        if get_decomposition_sum(i) == n:
            return i
    return 0 

def main():
    n = int(input())
    print(find_constructor(n))

if __name__ == '__main__':
    main()