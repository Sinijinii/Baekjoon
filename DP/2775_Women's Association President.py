T = int(input())
for tc in range(T):
    K = int(input())
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(K + 1)]
    for i in range(K+1):
        for j in range(n):
            cnt = 0
            #print("i: ",i)
            if i == 0:
                arr[i][j] = j + 1
                #print("0인경우 j의 값은 :",j+1)
            else:
                for num in range(j+1):
                    cnt += arr[i-1][num]
                arr[i][j] = cnt
                #print("0이 아닌경우 j의 값은: ",cnt)
    print(arr[K][n-1])