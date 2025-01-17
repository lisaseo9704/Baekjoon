import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    array = list(map(int, data[1:]))
    
    array.sort()
    
    for num in array:
        print(num)

if __name__ == "__main__":
    main()