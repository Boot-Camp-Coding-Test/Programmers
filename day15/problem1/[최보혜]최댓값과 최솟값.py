def solution(s):
    l = list(map(int, s.split(" ")))
    a,b = min(l), max(l)
    answer = str(a)+' '+str(b)
    return answer
