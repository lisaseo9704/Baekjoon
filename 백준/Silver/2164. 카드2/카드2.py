from collections import deque

def solve_card_game(n):
    queue = deque(range(1, n+1))
    tmp = queue[0]
    
    while len(queue) > 1:
        queue.popleft()
        
        if queue:
            card = queue.popleft()
            queue.append(card)
    
    return queue[0]


n = int(input())

print(solve_card_game(n))