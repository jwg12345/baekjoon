n = int(input())
m = int(input())

if m != 0:
    broke = list(input().split())
else:
    broke = []

ans = abs(n - 100)

for i in range(1000001):
    for j in str(i):
        if j in broke:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)