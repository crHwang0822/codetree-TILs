import sys


input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    str = list(input().split())
    func = str[0]

    if func == "push_back":
        a = int(str[1])
        arr.append(a)
    
    elif func == "pop_back":
        arr.pop()
    
    elif func == "size":
        print(len(arr))
    
    elif func == "get":
        k = int(str[1])
        print(arr[k-1])


