N = int(input())
stack = []
result = []
for i in range(N):
    value = input()
    if value[:4] == 'push':
        stack.append(value[5:])

    elif value == 'pop':
        if not stack:
            result.append(-1)
            continue
        pop = stack.pop()
        result.append(pop)

    elif value == 'size':
        length = len(stack)
        result.append(length)
    
    elif value == 'empty':
        if stack:
            result.append(0)
        elif not stack:
            result.append(1)
    
    elif value == 'top':
        if not stack:
            result.append(-1)
            continue
        result.append(stack[-1])

for res in result:
    print(res)