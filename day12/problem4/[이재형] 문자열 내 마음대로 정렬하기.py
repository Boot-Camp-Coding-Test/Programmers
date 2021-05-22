def solution(strings, n):
    answer = []
    result = []
    
    for i in strings :
        answer.append([i[n], i])
        
    a = sorted(answer)
    
    for i in a :
        result.append(i[1])  
    return result
