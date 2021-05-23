def solution(s):
    s = s.lower()
    s = list(s)
    
    return s.count('p') == s.count('y')
