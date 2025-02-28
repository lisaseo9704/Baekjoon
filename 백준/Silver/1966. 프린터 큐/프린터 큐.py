from collections import deque

def solution():
    test_cases = int(input())
    
    for _ in range(test_cases):
        n, m = map(int, input().split()) 
        priorities = list(map(int, input().split()))  
        
        documents = deque([(idx, prio) for idx, prio in enumerate(priorities)])
        
        count = 0  
        
        while documents:
            current = documents.popleft()
            
            if any(current[1] < doc[1] for doc in documents):
                documents.append(current)
            else:
                count += 1
                
                if current[0] == m:
                    print(count)
                    break

if __name__ == "__main__":
    solution()