n = int(input())

a = list(map(int, input().split()))
temp = []
result = []

for i in range(n):
    if i == n-1:
        result.append(-1)
        break
    for j in range(i+1, n):
        if a[i] < a[j]:
            temp.append(a[j])
            break # 오큰수 찾음
    else:
        temp.append(-1)
    result.append(temp[0])
    temp = [] #temp초기화
        
print(*result)
