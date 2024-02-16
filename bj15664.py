n, m = map(int, input().split())

a = sorted(list(map(int, input().split())))
p = []

flag = [0] * n

def dfs(start):
    check = 0
    if len(p) == m:
        print(*p)
        return

    for i in range(start, n):
        if check != a[i] and flag[i] == 0:
            p.append(a[i])
            flag[i] = 1
            check = a[i]    
            dfs(i)
            p.pop()
            flag[i] = 0

dfs(0)        