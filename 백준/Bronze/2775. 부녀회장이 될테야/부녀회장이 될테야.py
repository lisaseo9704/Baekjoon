T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    apartment = [[0] * (n+1) for _ in range(k+1)]
    
    for i in range(1, n+1):
        apartment[0][i] = i
    
    for floor in range(1, k+1):
        for room in range(1, n+1):
            apartment[floor][room] = sum(apartment[floor-1][1:room+1])
            # apartment[floor][room] = apartment[floor][room-1] + apartment[floor-1][room]
    
    print(apartment[k][n])