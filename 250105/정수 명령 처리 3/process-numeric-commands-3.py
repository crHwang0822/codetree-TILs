from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
    command = input()

    if command.startswith("push_front"):
        dq.appendleft(command.split()[1])
    elif command.startswith("push_back"):
        dq.append(command.split()[1])
    elif command.startswith("pop_front"):
        print(dq.popleft())
    elif command.startswith("pop_back"):
        print(dq.pop())
    elif command.startswith("size"):
        print(len(dq))
    elif command.startswith("empty"):
        if dq: print("0")
        else: print("1")
    elif command.startswith("front"):
        print(dq[0])
    else: 
        print(dq[-1])
    
    