import pprint
T = int(input())

pp_arr = [list(map(int,input().split())) for _ in range(T)]
arr = [[0]*100 for i in range(100)]

for idx in pp_arr:
    i = idx[0]
    j = idx[1]
    for di in range(0,10):
        for dj in range(0,10):
            arr[i+di][j+dj] = arr[i+di][j+dj] + 1

count = 0
a = 0
for i in arr:
    for j in i:
        if j == 1:
            count += 1
        if j > 1:
            count += (j-1)
print(count)