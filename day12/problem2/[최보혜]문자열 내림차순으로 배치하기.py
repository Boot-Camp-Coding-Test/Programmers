def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    return ''.join(map(str,answer))
