def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if not i % divisor: # 0으로 떨어질때
            answer.append(i)
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer
