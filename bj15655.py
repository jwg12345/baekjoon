n, m = map(int, input().split())

a = sorted(list(map(int, input().split())))
p = []


def dfs(start):
    if len(p) == m:
        print(*p)
        return

    for i in range(start, n):
        p.append(a[i])
        dfs(i+1)
        p.pop()

dfs(0)        


