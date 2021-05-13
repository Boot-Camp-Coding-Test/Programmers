def solution(a, b):
    sum = 0
    
    # a 가 작으면 아래 실행
    if a < b : 
        while a<=b :
            sum+=a
            a+=1
            
    # b 가 작으면 아래 실행
    else :
        while a>=b :
            sum+=b
            b+=1
    return sum
