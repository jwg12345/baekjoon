n = int(input())
wine = [0] #dp와 index를 맞추기 위한 더미 값
for i in range(n):
    wine.append(int(input()))

dp = [0] * (n + 1)
dp[1] = wine[1]
#n의 범위가 1 이상이라서 
if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i-2]+wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i])

print(dp[n])