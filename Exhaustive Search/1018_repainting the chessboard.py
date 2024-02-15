N,M = map(int,input().split()) # M×N 크기
arr = [list(input()) for _ in range(N)]
color = {'W':'B',
         'B':'A'}

for k in range(N):
    for i in range(M-8+1):
        for j in range(i,i+2):
            print(arr[k][j],end = " ")
        print()

# while i + 7 < N and j + 7 < M:
#
#     for idx in range(0,7):
#         if arr[i][j+idx] == arr[i][j+idx+1]:
#             arr[i][j+idx+1] = color[arr[i][j+idx]]
#     print(arr)
#     print("------------")
#     j+=1
#     i+=1