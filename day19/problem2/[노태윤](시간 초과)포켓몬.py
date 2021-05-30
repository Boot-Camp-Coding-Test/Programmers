from itertools import combinations
from collections import Counter

def solution(nums):
    combinations_list = list(combinations(nums,len(nums)//2))
    counter_list = list(map(lambda x : Counter(set(x)),combinations_list))
    answer = max(list(map(lambda x : sum(x.values()),counter_list)))
    return answer
