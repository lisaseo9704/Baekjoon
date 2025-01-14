def dfs(start, depth, n, m, result):
    if depth == m:
        print(' '.join(map(str, result)))
    else:
        for i in range(start, n+1):
            result.append(i)
            dfs(i+1, depth+1, n, m, result)
            result.pop()

n,m = map(int, input().split())
dfs (1, 0, n, m, [])