arr = input().split()
a = int(arr[0])
b = int(arr[1])

print(f"{3//5}.",end='')
r = 3%5 * 10

for _ in range(20):
    q = r//5
    r = r%5 * 10
    print(q,end='')