class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.next = None
            node.prev = None
        
        return next_node
    
    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        elif node == self.begin():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            node.prev.next = new_node
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
    
    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

import sys

input = sys.stdin.readline

nm = list(map(int,input().split()))
n = nm[0]
m = nm[1]
s = input()
dll = DLL()

for i in s:
    dll.push_back(i)

it = dll.end()

for _ in range(m):
    str = list(input().split())
    command = str[0]

    if command == "L":
        if it != dll.begin():
            it = it.prev
    
    elif command == "R":
        if it != dll.end():
            it = it.next

    elif command == "D":
        if it != dll.end():
            dll.erase(it)
    
    elif command == "P":
        dll.insert(it, str[1])

it = dll.begin()
while it != dll.end():
    print(it.data, end="")
    it = it.next