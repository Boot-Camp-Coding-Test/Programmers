def solution(a):
    answer = 0
    while a != 1:
        if a % 2 == 0 :
            a = a/2
            answer = answer + 1
        else :
            a = a * 3 + 1
            answer = answer + 1


    if answer > 500 :
        return -1
    else :
        return answer
