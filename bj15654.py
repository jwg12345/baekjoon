n, m = map(int, input().split())

a = list(map(int, input().split()))
p = []
a.sort()

def dfs(start):
    if len(p) == m:
        print(" ".join(map(str, p)))
        return

    for i in a:
        if i not in p:
            p.append(i)
            dfs(i+1)
            p.pop()

dfs(1)        