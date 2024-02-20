from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

p = permutations(a)
ans = 0

for i in p:
    s = 0
    for j in range(len(i) - 1):
        s += abs(i[j] - i[j+1])
    if s > ans:
        ans = s

print(ans)