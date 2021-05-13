case1

def solution(s):
    for i in range(len(s)):
        answer = ''
        if len(s) % 2 != 0:
            answer+=s[len(s)//2]
        else:
            answer+=s[len(s)//2-1:len(s)//2+1]
    return answer
  
  
  

  
case 2
  
def solution2(s):
  return s[(len(s)-1)//2:len(s)//2+1]
