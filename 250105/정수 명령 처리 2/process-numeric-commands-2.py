from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty():
            raise Exception()
        return self.dq.popleft()
    
    def front(self):
        if self.empty():
            raise Exception()
        return self.dq[0]

N = int(input())
q = Queue()

for _ in range(N):
    command = input()

    if command.startswith("push"):
        q.push(command.split()[1])
    elif command.startswith("pop"):
        print(q.pop())
    elif command.startswith("size"):
        print(q.size())
    elif command.startswith("empty"):
        print(q.empty()*1)
    else:
        print(q.front())
