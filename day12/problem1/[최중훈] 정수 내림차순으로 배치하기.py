def solution(n):
    tmp = [x for x in str(n)]
    answer = ''.join(list(reversed(sorted(tmp))))
    return int(answer)
