a = input()
cnt = 0 #막대기
stack = []

for i in range(len(a)):
    if a[i] == "(":
        stack.append("(")
    else:
        if a[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)
