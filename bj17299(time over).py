n = int(input())
a = list(map(int, input().split()))
result = [-1]*n
stack = [0]
cnt = []
for i in range(n):
    cnt.append(a.count(a[i])) #time over

for i in range(1, n):
    while stack and cnt[stack[-1]] < cnt[i]:
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)