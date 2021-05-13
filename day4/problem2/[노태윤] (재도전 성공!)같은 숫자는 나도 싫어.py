# 1~12 / 15~17 정확성 
# 2 효율성

def solution(arr):
    answer = []
    arr.insert(0,0)
    for i in range(1, len(arr)) : 
        if arr[i] == arr[i-1] :
            continue
        else :
            answer.append(arr[i])
        
    return answer

# =================================================

# 2차 도전

def solution(arr):
    answer = []
    
    # arr 첫번째 값 추가
    check_num = arr[0]
    answer.append(check_num)
    
    for i in arr : 
        
        # check_num 이랑 같다면 그냥 continue
        if i==check_num : 
            continue
            
        # 그 외에는 answer 에 append / check_num 업데이트
        else :
            answer.append(i)
            check_num=i
        
    return answer
