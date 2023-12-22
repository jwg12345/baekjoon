T = int(input())
result = []

for i in range(T):
    stack = []
    ps = input()
    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # if not stack
                result.append("NO")
                break
    else:
        if not stack:
            result.append("YES")
        else:
            result.append("NO")

for i in range(T):
    print(result[i])                