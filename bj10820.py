import sys
lower, upper, number, blank = [], [], [], []
while True:
    s = sys.stdin.readline().rstrip('\n') #줄바꿈 무시

    if not s:
        break

    l, u, n, b = 0, 0, 0, 0
    
    for i in s:
        if i.islower():
            l += 1
        elif i.isupper():
            u += 1
        elif i.isnumeric():
            n += 1
        elif i == ' ':
            b += 1
    lower.append(l)
    upper.append(u)
    number.append(n)
    blank.append(b)

for i in range(len(lower)):
    print(lower[i], upper[i], number[i], blank[i])