num = int(input())
for _ in range(num):
    line = input().split(' ')
    char_list = list(line[1])
    s = ''
    for i in range(len(char_list)):
        s += char_list[i]*int(line[0])
    print(s)