def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                sorted = False


n = int(input())
arr = list(map(int,input().split()))
bubble_sort(arr)

for i in arr:
    print(i, end=" ")