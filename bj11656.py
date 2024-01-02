s = input()

suffix = []

for i in range(len(s)):
    suffix.append(s[i:])

result = sorted(suffix)

for res in result:
    print(res)