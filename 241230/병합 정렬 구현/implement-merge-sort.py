def merge_sort(arr, low, high):
    if low<high:
        mid = (low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr, low, mid, high):
    i = low
    j = mid+1

    merged_arr = []

    while i<=mid and j<=high:
        if arr[i] < arr[j]:
            merged_arr.append(arr[i])
            i+=1
        else:
            merged_arr.append(arr[j])
            j+=1
    
    if i<=mid:
        merged_arr.extend(arr[i:mid+1])
    
    if j<=high:
        merged_arr.extend(arr[j:high+1])
    
    arr[low:high+1] = merged_arr

n = int(input())
arr = list(map(int,input().split()))

merge_sort(arr, 0, n-1)

for elem in arr:
    print(elem, end=" ")