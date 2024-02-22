T = 4
data = [list(map(int,input().split())) for _ in range(T)]
max_xy = 0
for max_v in data:
    if max_xy < max(max_v):
        max_xy = max(max_v)
arr = [[0 for _ in range(max_xy+1)] for __ in range(max_xy+1)]

for xy in data:
    #print(xy)
    for i in range(xy[0],xy[2]):
        for j in range(xy[1],xy[3]):
     #       print(i,j)
            arr[i][j] += 1
result = 0
for i in range(max_xy+500):
    for j in range(max_xy+500):
        if arr[i][j] != 0:
            result += 1

print(result)