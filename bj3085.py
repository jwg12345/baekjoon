def check(arr):
    n = len(arr)
    ans = 1

    for i in range(n):
        #열 순회
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            
            if  cnt > ans:
                ans = cnt
        #행 순회
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > ans:
                ans = cnt
    return ans

n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        #열 바꾸기
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            tmp = check(arr)
            if tmp > ans:
                ans = tmp
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        
        #행 바꾸기
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            tmp = check(arr)
            if tmp > ans:
                ans = tmp
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(ans) 