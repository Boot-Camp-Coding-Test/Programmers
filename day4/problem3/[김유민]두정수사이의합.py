def solution(a, b):
    answer = 0
    if a<=b :
        step = 1
    else :
        step = -1
        
    for num in range(a, b+step, step) :
        answer += num

    return answer
