def stacker(curr_index,last_index,prices) :
    if curr_index == last_index : # curr_index 가 마지막 index 면 그냥 0 반환
        return 0
  
    curr_price = prices[curr_index] # 특정 순간의 가격
    counts = 0

    for i in range(curr_index+1,last_index+1) : 
        counts+=1
        if curr_price > prices[i] : # 만약 한번이라도 curr_price 보다 떨어지면 for 문 break  
            break
            
    return counts

def solution(prices):
    last_index = len(prices) - 1
    curr_index = 0
    answer=[]
    
    for i in range(len(prices)) :
        answer.append(stacker(curr_index,last_index,prices)) # answer list 에 반복적으로 append 할 것
        curr_index+=1
        
    return answer
