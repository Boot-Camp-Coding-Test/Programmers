def solution(d, budget):
    d.sort()
    
    for i in range(len(d)):
        
        if budget >= sum(d):
            continue
        d = d[:-1]
        
    return len(d)


# 삽질흔적 / 시간초과
from itertools import combinations

def solution(d, budget):
    
    for n in range(len(d)):
        team = list(set(combinations(d, len(d) - n)))
        team = [sum(i) for i in team]
        
        if budget >= min(team):
            return len(d) - n
            
    return 0
