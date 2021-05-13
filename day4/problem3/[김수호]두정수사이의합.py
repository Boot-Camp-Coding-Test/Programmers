def solution(a, b):
    c = 0
    if a > b:
        c = b
        b = a
        a = c
    answer = 0
    for i in range(a, b+1):
        answer += i
    return answer
