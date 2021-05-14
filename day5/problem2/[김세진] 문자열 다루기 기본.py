def solution(s):
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
        if answer == True:
            return True
        else:
            return False
    else:
        return False
