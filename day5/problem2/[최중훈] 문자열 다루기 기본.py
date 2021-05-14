def solution(s):
    if len(s) == 4 or len(s) == 6:
        cnt = 0
        for char in s:
            try:
                char = int(char)
                cnt += 1
                if cnt == len(s) or cnt == len(s):
                    return True
            except:
                return False
    
    else: return False
