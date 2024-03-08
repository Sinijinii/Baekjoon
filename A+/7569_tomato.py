from collections import deque
# 3차원이니 z를 사용
dz = [0, 0, 0, 0, 1, -1]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]

def bfs():
    global day
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1
                if day < graph[nz][nx][ny]:
                    day = graph[nz][nx][ny]-1


m, n, h = map(int, input().split())
graph = []
queue = deque([])

# 3차원리스트로 받아주면서 queue에 익은 토마토의 장소를 저장해준다
for z in range(h):
    graph1 = []
    for x in range(n):
        graph1.append(list(map(int, input().split())))
        for y in range(m):
            if graph1[x][y] == 1:
                queue.append((z, x, y))
    graph.append(graph1)

# bfs 이후 모두 돌면서 max를 사용하는 것보다 빠를 것 같아 day 사용
day = 0
bfs()

# 안익읕 토마토가 있는지 확인하고 결과 값을 출력
for z in range(h):
    for x in range(n):
        if 0 in graph[z][x]:
            print(-1)
            # 모든 것을 종료(2중 for문 전체 종료) ↔ break는 for문 하나만 종료
            exit()
        if z == h-1 and x == n-1:
            print(day)


# 시간 초과
# from collections import deque
# M,N,H = map(int,input().split())
# arr = [[list(map(int,input().split())) for _ in range(N)] for __ in range(H)]
# # 익은 토마토 1. 익지 않은 토마토 0, 없는 경우 -1
# dx = [0,0,1,-1,0,0]
# dy = [1,-1,0,0,0,0]
# dz = [0,0,0,0,1,-1]
# arr = deque(arr)
# d = deque()
#
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if arr[i][j][k] == 0:
#                 d.append((i,j,k))
# cnt = 0
# while d:
#     cnt += 1
#     for i in range(H):
#         for j in range(N):
#             for k in range(M):
#                 for idx in range(6):
#                     if 0<=i+dx[idx]<H and 0<=j+dy[idx]< N and 0<=k+dz[idx]<M:
#                         if arr[i][j][k] == 1 and arr[i+dx[idx]][j+dy[idx]][k+dz[idx]] == 0:
#                             arr[i+dx[idx]][j+dy[idx]][k+dz[idx]]=1
#                             d.pop()
#     if cnt >= H*N*M//6:
#         cnt = -1
#         break
# print(cnt)
