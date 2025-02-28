import sys
K, N = map(int, input().split())
lan_lengths = [int(sys.stdin.readline()) for _ in range(K)]

start = 1  
end = max(lan_lengths) 

result = 0

while start <= end:
    mid = (start + end) // 2  
    count = sum(length // mid for length in lan_lengths)
    
    if count >= N:
        result = mid  
        start = mid + 1 
    else: 
        end = mid - 1  

print(result)