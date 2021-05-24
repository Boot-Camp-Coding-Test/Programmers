from itertools import combinations
def solution(nums):
    answer = 0
    l = list(set(combinations(nums, 3)))
    for i in range(len(l)):
        k, cnt = sum(l[i]), 0
        for j in range(2, int(k**0.5)+1):
            if k%j==0:
                cnt+=1
                break
        if cnt==0:
            answer+=1
    return answer
