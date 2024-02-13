n, m = map(int, input().split())

p = []

def dfs():
    if len(p) == m:
        print(" ".join(map(str, p)))
        return

    for i in range(1, n + 1):
        p.append(i)
        dfs()
        p.pop()

dfs()        