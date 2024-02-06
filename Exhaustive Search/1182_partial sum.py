N, S = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
# 비트연산자 사용하는 경우 빈 비트 연산자가 만들어져서, 0인 경우가 하나 존재함
if S == 0:
    result = -1
else:
    result = 0

for i in range(1<<N):
    sum_data = 0
    for j in range(N):
        if i & (1<<j):
            sum_data += arr[j]
    if sum_data == S:
        result += 1
print(result)
