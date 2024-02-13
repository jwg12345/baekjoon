n, m = map(int, input().split())

p = []

def dfs(start):
    if len(p) == m:
        print(" ".join(map(str, p)))
        return

    for i in range(start, n + 1):
        p.append(i)
        dfs(i)
        p.pop()

dfs(1)        