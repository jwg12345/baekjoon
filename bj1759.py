def dfs(cnt, idx):
    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(words[i])
        dfs(cnt + 1, i + 1) # 백트래킹
        answer.pop()

l, c = map(int, input().split())
words = sorted(list(map(str, input().split())))
vowel = ['a', 'e', 'i', 'o', 'u']
answer = []
dfs(0, 0)