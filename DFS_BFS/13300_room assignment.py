N, K = map(int, input().split()) # 수학여행에 참가하는 학생수, 한방에 배정할 수 있는 최대 인원수
S = []
Y = []
for _ in range(N):
    d = list(map(int, input().split()))
    S.append(d[0])
    Y.append(d[1])

year_list = []
room_cnt = 0
# 학년만큼
for y in range(1,7):
    # 각 학년에 맞는 인덱스 값 구하기
    y_list = list(filter(lambda x :Y[x] == y, range(N)))
    # 해당 인덱스에 속하는 남녀 성비 구하기
    count = 0
    for i in y_list:
        count += S[i]
    # 0과 1로 구성되어 있어 다 더한 값이 남자, 총 길이에서 다 더한값을 뺀 수가 여자로
    g = len(y_list) - count
    b = count
    # 남자 여자를 각 2명으로 나눈 몫을 더해줌
    room_cnt += g // K
    room_cnt += b // K
    # 만약 나머지가 있다면 +1을 해줌
    if g%K != 0:
        room_cnt += 1
    if b%K != 0:
        room_cnt += 1
print(room_cnt)



