from itertools import combinations

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append((i,j))
        elif arr[i][j] == 1:
            house.append((i,j))

result = 99999
for ch in combinations(chicken,M):
    result_list = []
    for hs in range(len(house)):
        min_dis = 99999
        dd = 0
        x, y = house[hs]
        for chick in ch:
            i, j = chick
            if (abs(x - i) + abs(y - j)) < min_dis:
                min_dis = abs(x - i) + abs(y - j)
        dd += min_dis
        result_list.append(dd)
    if result > sum(result_list):
        result = sum(result_list)

print(result)
