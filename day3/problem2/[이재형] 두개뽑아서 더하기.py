from itertools import combinations

def solution(numbers):
    
    a = list(combinations(numbers, 2))    
    answer = [(a[i][0] + a[i][1]) for i in range(len(a))]        
    answer = list(set(answer))

    return answer