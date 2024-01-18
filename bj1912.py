n = int(input())
number = list(map(int, input().split()))

sum = 0
tmp = []
for i in range(n):
    sum += number[i]
    tmp.append(sum)
    if sum < 0:
        tmp.append(sum)
        sum = 0

print(max(tmp))
    