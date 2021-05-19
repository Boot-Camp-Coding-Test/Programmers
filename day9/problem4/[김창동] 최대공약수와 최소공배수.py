from functools import reduce
# math logic

def solution(n, m):
    div, min_= 2, []

    while div < n+1 and div < m+1:
        if n % div == 0 and m % div == 0: # 공약수 산출
            n /= div
            m /= div
            min_.append(div)
            continue

        div += 1
        
    if len(min_):
        min_ = reduce(lambda x, y: x*y, min_)
    else:
        min_ = 1
    
    max_ = min_ * n * m
    return min_, int(max_)
