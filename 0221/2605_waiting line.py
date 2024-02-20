from collections import deque
N = int(input())
arr = list(map(int,input().split()))
st = deque(1 * i for i in range(1,N+1))
result = []
for i in range(N):
    if arr[i] == 0:
        result.insert(i,st[i])
    else:
        #print(st[i],arr[i])
        result.insert(st[i]-arr[i]-1,st[i])
print(*result)