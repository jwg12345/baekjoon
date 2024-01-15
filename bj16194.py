n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if dp[i] == 0:
            dp[i] = dp[i-j] + p[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + p[j])
print(dp[n])