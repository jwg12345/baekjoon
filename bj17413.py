stack = []
flag = False #괄호 안에 있는지 여부

s = input()
result = ''

for i in s:
    if i == "<":
        flag = True #괄호 안에 있음
        for _ in range(len(stack)):
            result += stack.pop()
    
    stack.append(i)

    if i == ">":
        flag = False
        for _ in range(len(stack)):
            result += stack.pop(0)
    
    if i == ' ' and flag == False:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '
print(''.join(list(result) + stack[::-1]))