n = int(input())
p = list(map(int, input().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if p[i] > p[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

res = []
M = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == M:
        res.append(p[i])
        M -= 1
res.reverse()
for r in res:
    print(r, end = ' ')

