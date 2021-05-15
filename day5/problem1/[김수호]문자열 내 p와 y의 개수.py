def solution(s):
    s = s.lower()
    answer = 0
    for i in list(s):
        if i == 'p':
            answer += 1
        elif i == 'y':
            answer -= 1
    if answer == 0:
        return True
    else : 
        return False
