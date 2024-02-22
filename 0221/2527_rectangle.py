T = 4
for tc in range(T):
    x1, y1, x2, y2, p1, q1, p2, q2 = map(int, input().split())
    result = 'a'
    if (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
        result = "c"
    if (x2 < p1) or (p2 < x1) or (q1 > y2) or (y1 > q2):
        result = "d"
    if p1 == x2 or x1 == p2 or y1 == q2 or y2 == q1:
        result = "b"

    print(result)




for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 공통부분이 없을 경우
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue
    # 한쪽 x만 같은 경우
    elif x1 == p2 or x2 == p1:
        # y도 같을 경우 점으로 만남
        if q1 == y2 or q2 == y1:
            print('c')
            continue
        # y가 다르면 선으로 만남
        else:
            print('b')
            continue
    # y쪽이 같을 경우
    elif q1 == y2 or q2 == y1:
        print('b')
        continue

    else:
        print('a')
        continue