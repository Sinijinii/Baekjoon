from collections import deque
N,K = map(int, input().split())
arr = deque(i for i in range(1,N+1))
result = []
idx = 0
for i in range(len(arr)):
    idx += K - 1
    print(idx)
    if idx > len(arr)-1:
        idx = idx - len(arr)
    if idx == len(arr):
        idx = 0

    print(idx)
    print("----")
    result.append(arr[idx])
    arr.remove(arr[idx])
print(result)
