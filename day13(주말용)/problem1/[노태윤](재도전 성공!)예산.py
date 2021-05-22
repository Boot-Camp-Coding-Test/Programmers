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

# ===========================================================================================
# 재도전 

def solution(d, budget):
    sorted_list = sorted(d) # 오름차순으로 정렬
    answer = 0
    summed = 0
    for i in sorted_list :
        summed+=i
        if summed < budget : # 합계가 budget 보다 미만이면 아래 코드 실행
            answer+=1
            continue
        elif summed == budget : # 합계가 budget 과 같다면 break
            answer+=1
            break
        else : # 합계가 budget 을 초과하면 break
            break
    return answer

# Key points
    # combinations 을 쓰다보니 모든 경우의 수를 반환해야되므로 시간이 오래 걸리는 것 같다
    # 어차피 최대 몇 개 부서에 물품을 지원할 수 있는지만 알면 되니까 오름차순으로 정렬하고 왼쪽부터 비교해서 풀면 됌
    
