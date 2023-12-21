T = int(input())
sentence = []

for i in range(T):
    sent = list(input().split())
    sentence.append(sent)

result = []
for i in range(T):
    for j in range(len(sentence[i])):
        res = sentence[i][j]
        # print(result[::-1])
        result.append(res[::-1])
     
for i in range(T):
    print(*result[:len(sentence[i])])
    del result[:len(sentence[i])]