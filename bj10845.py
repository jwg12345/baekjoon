N = int(input())
Q = []
result = []

for i in range(N):
    cmd = list(input().split())
    if cmd[0] == "push":
        Q.append(cmd[1])
        
    elif cmd[0] == "pop":
        if Q:
            result.append(Q[0])
            Q.pop(0)
        else:
            result.append(-1)

    elif cmd[0] == "size":
        result.append(len(Q))

    elif cmd[0] == "empty":
        if not Q:
            result.append(1)
        else:
            result.append(0)

    elif cmd[0] == "front":
        if Q:
            result.append(Q[0])        
        else:
            result.append(-1)

    elif cmd[0] == "back":
        if Q:
            result.append(Q[-1])
        else:
            result.append(-1)

for i in result:
    print(i)

    
