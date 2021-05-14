def solution(n):
    answer = 0
    
    if n == 1:
        return answer
    
    for i in range(2, n+1):
        tmp = 0
        for j in range(1, i+1):
            if i % j == 0:
                tmp += 1
        
        if tmp == 2:
            answer += 1
    
    return answer
     

################### 시간초과로 통과 못함 내일 다시..#####################    
