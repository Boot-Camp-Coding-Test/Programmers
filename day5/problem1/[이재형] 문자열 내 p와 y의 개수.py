def solution(s):
    answer = True
    s = s.lower()
    d = []
    for i in range(len(s)):
        if s[i] == 'p' :
            d.append(1)
        elif s[i] == 'y':
            d.append(-1)
            
    if (sum(d) == 0) or (d == None):
        
        return True
    else :
        return False