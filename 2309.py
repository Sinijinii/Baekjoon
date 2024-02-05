N_arr = 9
# 9난쟁이의 키 받기
data = []
for i in range(N_arr):
    data.append(int(input()))

# 최종 부분집합의 list
result = []
# 부분집합의 수만큼 반복(N_arr의 2승)
for i in range(1<<N_arr):
    sum_t = 0
    sum_pp = 0
    sum_data = []
    # 최대 0명부터 난쟁이의 수만큼의 부분집합의 원소가 생김
    for j in range(N_arr):
        if i & (1<<j):
            sum_t += data[j]
            sum_pp += 1
            sum_data.append(data[j])
    if sum_t == 100 and sum_pp == 7:
        result = sum_data

sort_list = sorted(result)
for i in sort_list:
    print(i)