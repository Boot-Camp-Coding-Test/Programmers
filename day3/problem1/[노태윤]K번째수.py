def solution(array,commands) : 
    answer = []
    for i in commands :
        # i 첫번째 값부터 두번째 값까지 추출 --> 정렬
        empty_list = sorted(array[i[0]-1:i[1]])
        # i 세번째 위치 값 append
        answer.append(empty_list[i[2]-1])

    return answer
