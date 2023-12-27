from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)

result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and count[a[stack[-1]]] < count[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)

print(*result)
