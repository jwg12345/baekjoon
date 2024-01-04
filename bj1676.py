n = int(input())
cnt = 0
f = 1
for i in range(1, n+1):
    f *= i

for i in range(len(str(f))):
    if f % 10 == 0:
        cnt += 1
    else:
        break
    f = f //10 
print(cnt)