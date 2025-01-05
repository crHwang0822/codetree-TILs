class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return not self.items
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()
    
    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]

N = int(input())

s = Stack()

for _ in range(N):
    command = input()

    if command.startswith("push"):
        s.push(command.split()[1])
    elif command.startswith("pop"):
        print(s.pop())
    elif command.startswith("size"):
        print(s.size())
    elif command.startswith("empty"):
        print(s.empty()*1)
    else:
        print(s.top())
    