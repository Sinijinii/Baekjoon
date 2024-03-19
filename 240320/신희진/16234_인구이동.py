def check(x, y):
    global res
    # 나와 이웃한 연합국가 선별을 위한 bfs
    Q = [(x, y)]
    vis[x][y] = 1
    # 상하좌우 확인
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    # 연합국가 인덱스를 담기 위함
    cd = []
    cd.append((x, y))
    cd_cnt = arr[x][y]
    while Q:
        i, j = Q.pop()
        for idx in range(4):
            if 0 <= i + di[idx] < N and 0 <= j + dj[idx] < N:
                if L <= abs(arr[i][j] - arr[i + di[idx]][j + dj[idx]]) <= R and vis[i + di[idx]][j + dj[idx]] == 0:
                    vis[i + di[idx]][j + dj[idx]] = 1
                    Q.append((i + di[idx], j + dj[idx]))
                    cd.append((i + di[idx], j + dj[idx]))
                    cd_cnt += arr[i + di[idx]][j + dj[idx]]
    return cd, cd_cnt


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

while True:
    vis = [[0 for _ in range(N)] for __ in range(N)]

    # 연합 국가를 찾기 위한 변수
    unions = []
    for i in range(N):
        for j in range(N):
            if vis[i][j] == 0:
                union, union_cnt = check(i, j)
                # 연합국가가 있을 경우 unions에 넣어줌
                if len(union) > 1:
                    unions.append((union, union_cnt))

    # 모든 연합국가를 찾은 후에 인구 이동 수행
    moved = False
    for union, union_cnt in unions:
        avg_population = union_cnt // len(union)
        for i, j in union:
            if arr[i][j] != avg_population:
                arr[i][j] = avg_population
                moved = True

    if not moved:
        break

    res += 1

print(res)
