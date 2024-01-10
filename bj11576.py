a, b = map(int, input().split())
m = int(input())
number = list(map(int, input().split()))[::-1]

x =0 
res = []

#a진법 -> 10진법
for i in range(m):
    x += number[i] * a ** i

#10진법 -> b진법
while x != 0:
    res.append(x % b)
    x = x // b

print(*res[::-1])


