def dfs(depth, idx):
    if depth == 6:
        print(*res)
        return

    for i in range(idx, k):
        res.append(s[i])
        dfs(depth + 1, i + 1)
        res.pop()

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    res = []
    dfs(0,0)
    if k == 0:
        exit()
    print()