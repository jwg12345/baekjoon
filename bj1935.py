n = int(input())
s = list(input())
num = [int(input()) for i in range(n)]

stack = []

for i in s:
    if i.isalpha():
        stack.append(num[ord(i)-65]) #A의 아스키코드 = 65
    else: #연산자라면
        a = stack.pop()
        b = stack.pop()

        if i == "+":
            b += a
        
        elif i == "-":
            b -= a
        
        elif i == "*":
            b *= a
        
        elif i == "/":
            b /= a
        
        stack.append(b)

print(f"{stack[-1]:.2f}")