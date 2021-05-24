# 1,6,7,9,13,23,24,25 실패
from collections import Counter
from operator import itemgetter

def solution(N, stages):
    cnt = dict(Counter(sorted(stages)))
    all_stages = [i for i in range(1, max(stages)+1)]
    for i in all_stages:
        if i not in cnt.keys():
            cnt[i] = 0

    cnt = sorted(cnt.items())
    prob = {}
    user_challenge = len(stages)

    for i in cnt:
        prob[i] = i[1] / user_challenge
        user_challenge -= i[1]
    
    prob_sorted = (sorted(prob.items(), key=itemgetter(1), reverse=True))
    answer = []
    
    for i in prob_sorted:
        if i[0][0] <= N:
            answer.append(i[0][0])
    
    return answer
  
