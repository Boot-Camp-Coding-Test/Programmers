def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        j = i
        
        while True:
            if i == n:
                cnt += 1
                break
            elif i > n:
                 break
            
            j += 1
            i += j
            
    return cnt
