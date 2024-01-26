n = int(input())
A = list(map(int, input().split()))
B = A[::-1]
dp1 = [1] * n #증가
dp2 = [1] * n #감소

for i in range(n):
    for j in range(i):
        if A[i] > A[j]: #증가
            dp1[i] = max(dp1[i], dp1[j] + 1)
        
        if B[i] > B[j]: #감소
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()

res = [0] * n
for i in range(n):
    res[i] = dp1[i] + dp2[i]

print(max(res) - 1)