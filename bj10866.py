from collections import deque
d = deque()
result = []

N = int(input())

for i in range(N):
    cmd = list(input().split())
    if cmd[0] == "push_front":
        d.appendleft(cmd[1])
    
    elif cmd[0] == "push_back":
        d.append(cmd[1])
    
    elif cmd[0] == "pop_front":
        if not d:
            result.append(-1)
        else:
            result.append(d[0])
            d.popleft()
    
    elif cmd[0] == "pop_back":
        if not d:
            result.append(-1)
        else:
            result.append(d[-1])
            d.pop()

    elif cmd[0] == "size":
        result.append(len(d))
    
    elif cmd[0] == "empty":
        if not d:
            result.append(1)
        else:
            result.append(0)
    
    elif cmd[0] == "front":
        if not d:
            result.append(-1)
        else:
            result.append(d[0])
    
    elif cmd[0] == "back":
        if not d:
            result.append(-1)
        else:
            result.append(d[-1])

for i in result:
    print(i)