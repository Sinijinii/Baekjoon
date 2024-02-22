N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for d in range(N):
    day = d + 1
    i = d
    mon = 0
    while day + arr[i][0] < N:
        mon += arr[i][1]
        day += arr[i][0]
        i += arr[i][0]
    print(mon)
    if result < mon:
        result = mon
    #print(i)
print(result)