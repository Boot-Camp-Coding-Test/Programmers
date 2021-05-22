def solution(d, budget):
    answer = 0
    if sum(d) <= budget :
        return len(d)
    else :
        d = sorted(d)
        while sum(d) > budget :
            d.pop()
        else :
            return len(d)
            
        
        
    
