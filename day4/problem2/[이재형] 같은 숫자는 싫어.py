

def solution(arr):
    
    for a in range(1, len(arr)) :
        if arr[a-1] != arr[a]:
            continue
        else :
            arr[a-1] = None
            
    answer = [i for i in arr if i != None]

    return answer        
