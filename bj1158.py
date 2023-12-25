N, K = map(int, input().split())
ppl = list(range(1, N+1))
idx = 0
result  = []

for i in range(N):
    idx = (idx + K - 1) % len(ppl)
    result.append(ppl.pop(idx))

print('<' + str(result)[1:-1] + '>')