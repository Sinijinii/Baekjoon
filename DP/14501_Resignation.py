N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
day = 0
i = 0
while day + arr[i][0] <= N:
    day += arr[i][0]

    print(i)
    print(day)