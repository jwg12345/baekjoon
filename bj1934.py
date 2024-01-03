T = int(input())
product, a, b = [], [], []
r = 0
gcd = [] #gcd 최대공약수

for i in range(T):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
    product.append(c*d)
    while True:
        r = a[i] % b[i]
        if r == 0:
            gcd.append(b[i])
            break
        a[i] = b[i]
        b[i] = r

for i in range(T):
    print(product[i] // gcd[i])

