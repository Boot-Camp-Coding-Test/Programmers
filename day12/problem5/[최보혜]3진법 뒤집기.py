def solution(n):
    l = []
    while n!=0:
        res = n%3
        n //=3
        l.append(res)
    answer = ''.join(map(str, l))
    answer = int(answer,3)
    return answer
