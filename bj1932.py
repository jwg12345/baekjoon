n = int(input())

dp = [[0] * n for _ in range(n)]
number = []
for i in range(n):
    number.append(list(map(int, input().split())))

dp[0][0] = number[0][0]

# 첫 번째 행의 값 계산
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + number[i][0]
    dp[i][i] = dp[i-1][i-1] + number[i][i]

# 나머지 행의 값 계산
for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + number[i][j]

# 마지막 행에서 최대값 찾기
answer = max(dp[n-1])

print(answer)
