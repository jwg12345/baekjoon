import sys
a = list(input())
N = len(a)
M = int(input())
cursor = N # index로 보기

for i in range(M):
    # cmd = list(input().split())
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "L":
        if cursor == 0:
            continue
        else:
            cursor -= 1
    
    elif cmd[0] == "D":
        if cursor == N:
            continue
        else:
            cursor += 1
    
    elif cmd[0] == "B":
        if cursor == 0:
            continue
        else:
            a.remove(a[cursor-1])
            cursor -= 1
    
    elif cmd[0] == "P":
        a.insert(cursor, cmd[1])
        cursor += 1

print("".join(a))
