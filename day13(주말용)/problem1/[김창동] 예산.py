def solution(d, budget):
    d.sort()
    
    for i in range(len(d)):
        
        if budget >= sum(d):
            continue
        d = d[:-1]
        
    return len(d)
