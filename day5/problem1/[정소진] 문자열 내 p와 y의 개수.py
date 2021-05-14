def solution(str):
    
    str = str.lower()
    
    cnt_p, cnt_y = 0, 0
    
    for s in str:
        if s == 'p': cnt_p += 1
        elif s == 'y': cnt_y += 1
    
    if cnt_p == cnt_y: return True

    return False
