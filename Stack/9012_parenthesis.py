T = int(input())
# 딕셔너리의 키, 데이터 형태로 각 괄호의 짝을 둠
parenthesis = {'(':')'}

for tc in range(T):
    str_data = input()
    # 괄호의 경우 담아둘 스택
    par_check_stack = []
    # 기본적인 result값을 -로 설정
    result = '-'
    # 데이터를 순회
    for i in str_data:
        # 데이터의 값이 괄호 딕셔너리의 키값에 있다면
        # 스택에 해당 키의 짝인 데이터값(닫히는 괄호)을 넣어줌
        if i in parenthesis:
            par_check_stack.append(parenthesis[i])
        # 만약 데이터의 값이 괄호딕셔너리의 데이터 값(닫히는 괄호)이며,
        # 스택이 빈값이 아니며, 그 값이 스택의 마지막 값이라면 스택에서 삭제해줌
        if i in parenthesis.values():
            if len(par_check_stack) != 0 and i == par_check_stack[-1]:
                par_check_stack.pop()
            # 그렇지 않다면 > 스택이 비어있거나, 값이 스택의 마지막값이 아니라면
            # result에 0을 반환해줌
            else:
                result = 0
                break
    # 최종적으로 만들어진 스택은 비어있고, result의 값이 초기값과 같다면 성공
    if len(par_check_stack) == 0 and result =='-':
        result = 'YES'
    # 스택이 차있거나, 순서의 문제 혹은 짝 없는 닫히는 괄호의 존재로 result의 값이 0이 되었다면
    # 그 값 그대로 실패
    else: result = 'NO'

    print(result)




