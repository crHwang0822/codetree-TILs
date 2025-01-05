from collections import deque

n = int(input())

dq = deque()

for i in range(n):
    dq.append(i+1)

while len(dq)>1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])