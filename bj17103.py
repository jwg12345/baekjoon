import sys
number = [True] * 1000001

#에라토스테네스의 체
for i in range(2, int(len(number)**0.5)+1):
    if number[i]:
        for j in range(2*i, 1000001, i):
            number[j] = False

t = int(input())
for i in range(t):
    cnt = 0
    n = int(input())
    for j in range(2, n//2+1):
        if number[j] and number[n-j]:
            cnt += 1
    print(cnt)