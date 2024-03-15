#기준점 (x, y)와 경계의 길이 d1, d2를 정한다.
# (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
# 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
# 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
def district(x,y,d1,d2):
    dis = [0,0,0,0,0]
    for r in range(N):
        for c in range(N):
            cnt = arr[r][c]
            if r < x + d1 and c <= y:
                if r + c >= x + y:
                    dis[4] += cnt
                else:
                    dis[0] += cnt
            elif r <= x + d2 and y < c:
                if r - c >= x - y:
                    dis[4] += cnt
                else:
                    dis[1] += cnt
            elif x + d1 <= r and c < y - d1 + d2:
                if r - c <= x - y + (2 * d1):
                    dis[4] += cnt
                else:
                    dis[2] += cnt
            elif x + d2 < r and y - d1 + d2 <= c:
                if r + c <= x + y + (2 * d2):
                    dis[4] += cnt
                else:
                    dis[3] += cnt
            else:
                dis[4] += cnt
    return dis

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 9999999
for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1 <= x < x+d1+d2<=N and 1 <= y-d1 <y <y+d2 <=N:
                    dis = district(x,y,d1,d2)
                    if max(dis)-min(dis) < result:
                        result = max(dis)-min(dis)
print(result)