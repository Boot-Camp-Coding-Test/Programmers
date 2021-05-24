def solution(n):
    l = list(map(int, str(n)))
    l.sort(reverse=True)
    answer = ''.join(map(str, l))
    return int(answer)
