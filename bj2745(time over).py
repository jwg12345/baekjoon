import sys
n, b = sys.stdin.readline().split()
b = int(b)
res = 0
l = len(n)
for i in range(l): #0~4
    if ord(n[l-i-1]) >= 65:
        res += ((ord(n[l-i-1])-55) * pow(b, i))
    else:    
        res += int(n[l-i-1] * pow(b, i))

print(res)