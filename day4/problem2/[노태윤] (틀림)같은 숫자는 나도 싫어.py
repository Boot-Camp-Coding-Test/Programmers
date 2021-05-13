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
