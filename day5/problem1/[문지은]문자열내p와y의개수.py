#case1
import collections

def solution(s):
    upper_s = s.upper()
    a = collections.Counter()
    a.update(upper_s)

    return a['P']==a['Y']


#case2  
def solution2(s):
  s = s.upper()
  s = s.count('P') == s.count('Y')
  return s


#case3
def solution3(s):
  return s.upper().count('P') == s.upper().count('Y')

solution(s)
