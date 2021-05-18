def solution(n):
    answer = '수박'*(n//2)
    if n%2==0:
        return answer
    else:
        return answer+'수'
