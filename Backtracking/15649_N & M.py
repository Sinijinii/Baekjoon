N,M = map(int,input().split())

arr = list(range(1,4))
for i in range(1<<N):
    for j in range(N):
        if i & j<<1:
            print(arr[j])