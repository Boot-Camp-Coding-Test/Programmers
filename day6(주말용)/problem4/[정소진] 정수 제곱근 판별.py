import math
def solution(n):
    
    sqrt_n = math.sqrt(n)
    
    if int(sqrt_n) == sqrt_n:
        return (sqrt_n + 1)**2
    
    return -1
