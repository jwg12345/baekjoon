a, b = map(int, input().split())
product = a * b
r = 0
gcd = 0 #최대공약수
while True:
    r = a % b
    if r == 0:
        gcd = b
        break
    a = b
    b = r

lcm = product // gcd

print(gcd)
print(lcm)