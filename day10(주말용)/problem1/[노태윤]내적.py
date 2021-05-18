def solution(a, b):
    answer = 0
    for i in range(len(a)) : 
        multiplied = a[i] * b[i]
        answer+=multiplied
    return answer
