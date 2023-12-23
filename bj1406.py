import sys

left = list(input())
right = []

for _ in range(int(input())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "L" and left:
        right.append(left.pop())
    elif cmd[0] == "D" and right:
        left.append(right.pop())
    elif cmd[0] == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[1])

ans = left  + right[::-1]
print("".join(ans))
