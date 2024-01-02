a, b, c, d = map(int, input().split())

sum1 = (a * (10**len(str(b)))) + b 
sum2 = (c * (10**len(str(d)))) + d
print(sum1 + sum2)
