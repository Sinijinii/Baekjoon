target = int(input())
# 타겟을 0부터 돌기
for i in range(target):
    # 분해합을 구하기 245 >2+4+5
    temp = sum(map(int, str(i)))
    # 분해합과 나 자신을 더하기
    result = i + temp
    # 값 비교
    if result == target:
        print(i)
        break
else:
    print(0)
