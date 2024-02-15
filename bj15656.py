n, m = map(int, input().split())

a = sorted(list(map(int, input().split())))
p = []

def dfs(start):
    if len(p) == m:
        print(" ".join(map(str, p)))
        return

    for i in a:
        p.append(i)
        dfs(i)
        p.pop()

dfs(1)