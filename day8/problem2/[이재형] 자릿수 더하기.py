def solution(n):

    return sum([int(list(str(n))[i]) for i in range(len(list(str(n))))])