n = int(input())
stack = []
a = []
flag = True
cnt = 1

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        a.append("+")
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        a.append("-")
    else:
        flag = False

if not flag: # flag == False
    print("NO")
else: #flag == True
    for i in a:
        print(i)