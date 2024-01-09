n, b = map(int, input().split())

res = ''
while True:
    if n < b:
        res += chr(ord('A') + n - 10) if n >= 10 else str(n)
        break
    r = n % b
    if r >= 10:
        res += chr(ord('A') + r - 10)
    else:
        res += str(r)
    n = n // b

print(res[::-1])