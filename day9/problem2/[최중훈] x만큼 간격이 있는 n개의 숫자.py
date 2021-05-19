def solution(x, n):
    answer = list(map(lambda a: a*x, [i for i in range(1, n+1)]))

    return answer
