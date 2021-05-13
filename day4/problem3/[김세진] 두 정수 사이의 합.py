def solution(a,b):
  answer = 0
  if a==b:
    answer = a
  elif b>a:
    answer = int((b/2*(b+1))-(a/2*(a+1))+a)
  else:
    answer = int((a/2*(a+1))-(b/2*(b+1))+b)
  return answer
