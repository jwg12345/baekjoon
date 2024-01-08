n = int(input())

ans = ''

if n == 0:
    print(0)

while n:
    if n % (-2) != 0:
        ans += '1'
        n = n//-2 + 1
    else:
        ans += '0'
        n = n//-2

print(ans[::-1])
