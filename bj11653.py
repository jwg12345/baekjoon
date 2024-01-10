n = int(input())

if n == 1:
    print()

result = []
for i in range(2, n + 1):
    if n % i == 0:
        # i로 나눌 수 없을 때 까지 나누기
        while n % i == 0:
            n = n // i
            result.append(i)

for res in result:
    print(res)