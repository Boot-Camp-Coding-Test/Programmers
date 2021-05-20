from itertools import combinations

def isprime(num,counts=0) :
  
    # 2부터 num-1 까지 num 에서 나눌 때 하나라도 나누어 떨어지는게 있다면 0 반환
    for i in range(2,num) :
        if num % i == 0 :
            return counts
    
    # 소수라면 1 반환
    else :
        counts=1
    return counts

def solution(nums):
    answer=0
    
    # 3개로 묶을 수 있는 조합 리스트 반환
    combinations_list = list(combinations(nums,3))
    
    # 각 element 의 합 구해서 반환
    add_combinations_list = list(map(lambda x: x[0] + x[1] + x[2],combinations_list))
    
    # 이들 중 소수가 있다면 1 씩 증가
    for i in add_combinations_list :
        answer += isprime(i)

    return answer
