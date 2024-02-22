di = [0,1,0,-1]
dj = [1,0,-1,0]
# R과 C가 바뀌어야 코드상으로 같아짐
C,R = map(int,input().split())
K = int(input())
arr = [[0 for i in range(R)] for _ in range(C)]
i = 0
x, y = 0,0
cnt = 1
ni = x
nj = y
arr[0][0] = 1
result = [0]
if K == 1:
    print(ni+1,nj+1)
else:
    for _ in range(1,C*R+100):
        ni += di[i]
        nj += dj[i]
        if 0 <= ni < C and 0 <= nj < R and arr[ni][nj] == 0:
            cnt += 1
            arr[ni][nj] = cnt
        else:
            ni -= di[i]
            nj -= dj[i]
            i = i+1
            if i == 4:
                i = 0
        if cnt == K:
            result[0] = ni + 1
            result.append(nj + 1)
            break
    print(*result)

