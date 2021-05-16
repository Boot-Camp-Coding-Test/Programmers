def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        divisors_lst =  [j for j in range(1, i+1) if i % j == 0]
        if len(divisors_lst) % 2 == 0:
            answer += i
        else:
            answer -= i 
    
    return answer
