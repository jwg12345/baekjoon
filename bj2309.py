a = []
for i in range(9):
    a.append(int(input()))

a.sort()
s = sum(a)

x, y = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if s - (a[i] + a[j]) == 100:
            x, y = a[i], a[j]
a.remove(x)
a.remove(y)

for i in a:
    print(i)