def solution(n):
    answer = 1
    prev = 0
    for num in range(1, n+1) :
        if num == 1 :
            continue
        if num == 2 :
            prev = 1
        else :
            temp = answer
            answer = prev + answer
            prev = temp
    
    return answer % 1234567
