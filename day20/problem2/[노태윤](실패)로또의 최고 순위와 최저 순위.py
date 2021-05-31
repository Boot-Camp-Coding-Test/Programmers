# test 14 실패

def solution(lottos, win_nums):
    answer = []
    common_number_counts = len(set(lottos) & set(win_nums))
    zero_counts = lottos.count(0)
    answer.append(7-(common_number_counts + zero_counts))
    if common_number_counts <= 1 :
        answer.append(6)
    else :
        answer.append(7-common_number_counts)
    return answer
