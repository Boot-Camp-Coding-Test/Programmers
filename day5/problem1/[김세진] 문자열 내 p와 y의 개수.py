def solution(s):
    p = 0
    y = 0
    
    s = s.lower()
    
    for i in range(len(s)):
        if s[i] == 'p':
            p+=1
        elif s[i] == 'y':
            y+=1
    
    if p==0 and y==0:
        return True
    elif p==y:
        return True
    elif p!=y:
        return False
