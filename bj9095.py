t = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = sum(dp[i-3:i])

result = []
for _ in range(t):
    result.append(dp[int(input())])

for res in result:
    print(res)
