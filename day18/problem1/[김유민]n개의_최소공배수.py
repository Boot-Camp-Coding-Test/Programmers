from math import gcd
def solution(arr):
    if len(arr) == 1:
        return arr
    
    elif len(arr) == 2:
        return int((arr[0]*arr[1])/gcd(arr[0], arr[1]))
        
    else :
        mid_index = int(len(arr)/2)
        answer = solution([solution(arr[:mid_index+1]), solution(arr[mid_index:])])
        
    return answer
