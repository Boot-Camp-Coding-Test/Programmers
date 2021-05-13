# 1부터 n까지 더하는 공식 : n/2*(n+1)
# a부터 b까지의 숫자들을 다 더하려면, 1부터 b까지 전부다 더한 값에서 1부터 a까지 전부다 더한 값을 빼서 거기다 a를 더하면 됨

def solution(a,b):
  answer = 0
  if a==b:
    answer = a
  elif b>a:
    answer = int((b/2*(b+1))-(a/2*(a+1))+a)
  else:
    answer = int((a/2*(a+1))-(b/2*(b+1))+b)
  return answer

