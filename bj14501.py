n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]

for i in range(n):
    t, p = map(int, input().split())
    T[i]= t
    P[i] = p

dp = [0 for i in range(n + 1)]

for i in range(n - 1, -1, -1):
    if T[i] + i > n:
        dp[i] = dp[i+1]
    
    else:
        dp[i] = max(dp[i+1], dp[T[i] + i] + P[i])

print(dp[0])