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
    def front(self):
        if self.empty():
            raise Exception()
        return self.dq[0]
    def pop(self):
        if self.empty():
            raise Exception()
        return self.dq.popleft()


n, k = tuple(map(int,input().split()))
q = Queue()

for i in range(n):
    q.push(i+1)

while not q.empty():
    for _ in range(k-1):
        q.push(q.front())
        q.pop()
    print(q.pop(), end=" ")

