import math
n, s = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = abs(s - a[i])

ans = a[0]
for i in range(1, n):
    ans = math.gcd(ans, a[i])

print(ans)
