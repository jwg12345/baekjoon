n = int(input())
p = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if p[i-1] > p[i]:
        for j in range(n-1, 0, -1):
            if p[i-1] > p[j]:
                p[i-1], p[j] = p[j], p[i-1]
                p = p[:i] + sorted(p[i:], reverse = True)
                print(*p)
                exit()

print(-1)

