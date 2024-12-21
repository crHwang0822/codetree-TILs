import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        else:
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
        
        self.node_num += 1
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        
        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            return
        elif self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1
            return temp.data
    
    def pop_back(self):
        if self.tail == None:
            return
        elif self.tail.prev == None:
            temp =self.tail
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1
            return temp.data
    
    def size(self):
        return self.node_num
    
    def empty(self):
        return 1 if self.node_num == 0 else 0
    
    def front(self):
        if self.head == None:
            return
        else:
            return self.head.data
    
    def back(self):
        if self.tail == None:
            return
        else:
            return self.tail.data

input = sys.stdin.readline

n = int(input())

l = DoublyLinkedList()

for _ in range(n):
    str = list(input().split())
    command = str[0]

    if command == "push_front":
        l.push_front(str[1])
    elif command == "push_back":
        l.push_back(str[1])
    elif command == "pop_front":
        print(l.pop_front())
    elif command == "pop_back":
        print(l.pop_back())
    elif command == "size":
        print(l.size())
    elif command == "empty":
        print(l.empty())
    elif command == "front":
        print(l.front())
    elif command == "back":
        print(l.back())