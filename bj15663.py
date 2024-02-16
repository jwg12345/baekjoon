n, m = map(int, input().split())

a = sorted(list(map(int, input().split())))
p = []

flag = [0] * n

def dfs():
    check = 0
    if len(p) == m:
        print(*p)
        return

    for i in range(n):
        if check != a[i] and flag[i] == 0:
            p.append(a[i])
            flag[i] = 1
            check = a[i]    
            dfs()
            p.pop()
            flag[i] = 0

dfs()        