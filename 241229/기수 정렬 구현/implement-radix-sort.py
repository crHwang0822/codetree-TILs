# 상수 선언 
MAX_K = 6
MAX_DIGIT = 10

# 입력
n = int(input())
arr = list(map(int,input().split()))

def radix_sort():
    global arr
    for pos in range(MAX_K):
        arr_new = [[] for i in range(MAX_DIGIT)]
        for i in range(len(arr)):
            digit = (arr[i]//10**pos)%10
            arr_new[digit].append(arr[i])
        
        store_arr = []
        for digit in range(MAX_DIGIT):
            for j in range(len(arr_new[digit])):
                store_arr.append(arr_new[digit][j])
        
        arr = store_arr

radix_sort()
for elem in arr:
    print(elem, end=" ")
    