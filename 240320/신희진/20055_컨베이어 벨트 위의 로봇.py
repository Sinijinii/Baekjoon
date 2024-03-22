from collections import deque
import sys
input1 = sys.stdin.readline
N,K = map(int,input().split())


ro = deque(0 for _ in range(N))
con = deque(map(int,input().split()))

res = 0
cnt = 0
while cnt < K:

    res += 1

    con.rotate(1)

    ro.pop()
    ro.insert(0,0)

    ro[-1] = 0
    for i in range(N-2,-1,-1):
        if ro[i] == 1:
            if ro[i+1] != 1 and con[i+1] != 0:
                ro[i] = 0
                ro[i+1] = 1
                con[i+1] -= 1
                if con[i+1] == 0:
                    cnt += 1


    if con[0] != 0:
        con[0] -= 1
        ro[0] = 1
        if con[0] == 0:
            cnt += 1

print(res)
