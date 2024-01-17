n = int(input()) 
#끝자리가 0이면 2개 1이면 1개
dp = [0 for _ in range(91)]
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

