n = int(input())
number = list(map(int, input().split()))

dp =[[0] * n for _ in range(2)]
dp[0][0] = number[0] #제거 x
dp[1][0] = -1000 #제거 o

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + number[i], number[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + number[i])

print(max(max(dp[1]), max(dp[0])))