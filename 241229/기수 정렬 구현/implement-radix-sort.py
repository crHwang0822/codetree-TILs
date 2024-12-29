# 상수 선언 
MAX_K = 6
MAX_DIGIT = 10

# 입력
n = int(input())
arr = list(map(int,input().split()))

def radix_sort(arr):
    for pos in range(MAX_K):
        arr_new = [[] for i in range(MAX_DIGIT)]
        for i in range(len(arr)):
            digit = (arr[i]//10**pos)%10
            arr_new[digit].append(arr[i])
        
        i = 0
        for digit in range(MAX_DIGIT):
            for j in range(len(arr_new[digit])):
                arr[i] = arr_new[digit][j]
                i += 1
        

radix_sort(arr)
for elem in arr:
    print(elem, end=" ")
    