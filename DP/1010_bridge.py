def factorial(N):
    result = 1
    for i in range(1,N+1):
        result *= i
    return result

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M)/(factorial(M-N)*factorial(N))))