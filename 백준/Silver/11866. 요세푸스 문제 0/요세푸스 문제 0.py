from collections import deque

def josephus(N, K):
    queue = deque(range(1, N + 1))
    result = []
    
    while queue:
        for _ in range(K - 1):
            queue.append(queue.popleft())

        result.append(queue.popleft())
    
    return result

def main():

    N, K = map(int, input().split())

    answer = josephus(N, K)
    
    print('<' + ', '.join(map(str, answer)) + '>')

if __name__ == "__main__":
    main()