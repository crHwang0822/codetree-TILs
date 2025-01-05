class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def empty(self):
        return not self.items
    def pop(self):
        if self.empty():
            raise Exception()
        return self.items.pop()
    def size(self):
        return len(self.items)
    def top(self):
        if self.empty():
            raise Exception()
        return self.items[-1]

def solution(arr):
    s = Stack()

    for elem in arr:
        if elem == "(":
            s.push("(")
        else:
            if s.empty():
                return "No"
            s.pop()
    
    if not s.empty():
        return "No"
    
    return "Yes"

str = list(input())
print(solution(str))