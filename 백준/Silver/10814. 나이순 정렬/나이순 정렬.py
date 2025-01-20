n = int(input())  
members = []

for _ in range(n):
    age, name = input().split()
    age = int(age) 
    members.append((age, name))  

sorted_members = sorted(members, key=lambda x: x[0])

for age, name in sorted_members:
    print(age, name)