# 1
def solution(n):
    int_list = [num for num in str(n)]
    int_list.sort(reverse=True)
    
    length = len(int_list) - 1
    answer = 0
    for num in int_list:
        answer += int(num) * (10 ** length)
        length -= 1
    
    return answer

  
  # 2
  def solution(n):
    length = len(str(n))
    int_list = sorted([int(str(n)[i]) for i in range(length)], reverse=True) 
    answer_list = list(map(lambda x, y : x * (10 ** (y-1)), int_list, range(length, 0, -1)))
    return sum(answer_list)
