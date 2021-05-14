from collections import Counter
def solution(s):
    s_lst = [i for i in s.lower()]
    cnt = Counter(s_lst)
    
    if cnt['p'] == cnt['y']:
        return True
    
    else: return False
