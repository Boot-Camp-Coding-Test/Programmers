from itertools import combinations

def check_prime(num):
    lst = []
    for i in range(1, num+1):
        if num % i == 0:
            lst.append(i)
    if len(lst) == 2:
        return True
    else:
        return False

def solution(nums):
    answer = 0
    three_num_comb = list(combinations(nums, 3))
    for comb in three_num_comb:
        if check_prime(sum(comb)):
            answer += 1

    return answer 
