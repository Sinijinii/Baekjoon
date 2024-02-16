T = int(input())
for tc in range(T):
    # 시험장 수
    N = int(input())
    # 응시자 수
    A = list(map(int,input().split()))
    # 총감독관이 감시할 수 있는 응시자 수 B, 부감독관이 감시할 수 있는 응시자 수 C
    B,C = map(int, input().split())
    result = 0
    for i in A:
        if i - B < 0 :
            cnt = 0

        elif (i-B) % C != 0:
            cnt = ((i - B) // C) + 1

        elif (i-B) % C == 0:
            cnt = ((i - B) // C)
        result += cnt
    print(result + N) # > 총감독관 수 더해주기
