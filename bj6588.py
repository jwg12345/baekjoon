import sys
number = [True] * 1000001

#에라토스테네스의 체
for i in range(2, int(len(number)**0.5)+1):
    if number[i]:
        for j in range(2*i, 1000001, i):
            number[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, int(len(number)**0.5), 2): #홀수소수->3부터 시작 하고짝수는 건너 뛰기위해 2칸씩
        if number[i] == 1 and number[n - i] == 1:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")


