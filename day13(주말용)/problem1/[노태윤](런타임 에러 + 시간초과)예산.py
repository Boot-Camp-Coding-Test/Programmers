# 테스트 3 런타임 에러 / 테스트 7 ~23 시간 초과

from itertools import combinations

def solution(d, budget):
    length = len(d)
    for i in range(1,length+1) :
        combinations_list = list(combinations(d,i))
        summed_combinations_list = list(map(lambda x : sum(x),combinations_list))
        true_false_list = [True if i<=budget else False for i in summed_combinations_list]
        if True in true_false_list :
            answer = i
    return answer
