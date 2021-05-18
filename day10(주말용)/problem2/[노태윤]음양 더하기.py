def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :
        
        # 해당 위치에 있는 값이 True 면 더하기
        if signs[i]==True :
            answer+=absolutes[i]
           
        # False 면 빼기
        else :
            answer-=absolutes[i]
    return answer
