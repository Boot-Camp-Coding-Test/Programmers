# 테스트 7 ~ 20 시간 초과

from itertools import combinations
from collections import Counter

def solution(nums):
    combinations_list = list(combinations(nums,len(nums)//2))
    counter_list = list(map(lambda x : Counter(set(x)),combinations_list))
    answer = max(list(map(lambda x : sum(x.values()),counter_list)))
    return answer

# ==========================================================================
# 재도전 

def solution(nums):
    set_list = list(set(nums)) # 모든 종류 가 담긴 리스트 반환
    if len(set_list) <= len(nums)//2 : 
        return len(set_list) # 만약 set_list 의 길이 (모든 종류 갯수) 가 N/2 보다 작거나 같다면 모든 종류 갯수 반환
    else :
        return len(nums)//2 # 아니면 N/2 반환
    
# Key points
    # 조금만 생각해보면 답을 쉽게 구할 수 있었던 문제다..
    
    # 처음 풀었던 것도 알고리즘은 맞게 구현한 것 같다 (아닐수도..). 하지만 효율성 면에서 좋지 않았음
    
    # ex) nums = [1,2,3,3]
        # 이 때 모든 종류 갯수는 1,2,3 ==> 3 가지 임 
        # 그런데 4/2 ==> 2 포켓몬만 뽑는 것이기 때문에 가장 많은 종류의 포켓몬을 선택하는 방법도 2 가지 임 
        
    # ex) nums = [1,1,1,2,2,2,3,3,3,4]
        # 이 때 모든 종류 갯수는 1,2,3,4 ==> 4 가지 임
        # 그런데 10/2 ==> 5 포켓몬을 뽀는 과정에서 1 종류는 무조건 중복으로 겹침 (가장 많은 종류의 포켓몬 선택할 때)
        # 그래서 최대로 뽑을 수 있는 종류 수는 4 가지 임
    
    # set, list, 만으로 풀 수 있음
    
