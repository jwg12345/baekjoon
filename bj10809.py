s = input()
location = [-1]*26

for i in s:
    location[ord(i)-97] = s.index(i)
print(*location)
