def solution(n):
    answer = []
    
    # 이렇게 하면 ['1','2','3','4','5'] 형태로 나옴
    splitted = list(str(n))
    
    # 마지막 index 반환
    length = len(splitted)-1
    
    # 마지막 index 부터 0까지 -1 씩 감소하는 for loop
    for i in range(length,-1,-1) :
      
        # answer list 
        answer.append(int(splitted[i]))
        
    return answer
