import math

t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    n, nums, res = a[0], a[1:], 0

    for j in range(n-1):
        for k in range(j+1, n):
            res += math.gcd(nums[j], nums[k])
    print(res)