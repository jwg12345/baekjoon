def num(M, N, x, y):
    while x <= M * N:
        if abs(x - y) % N == 0:
            return x
        x += M
    return -1

t = int(input())
for _ in range(t):
    M,N,x,y = map(int, input().split())
    print(num(M,N,x,y))