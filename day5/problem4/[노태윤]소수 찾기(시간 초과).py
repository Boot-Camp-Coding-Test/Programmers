# test 10~12 실패 (시간초과)
# 효율성 1~4 실패 (시간초과)
  
def isprime(N) :
    if N == 1 :
        return 0
    count=0
    for i in range(1,N+1) :
        if N % i == 0 :
            count+=1
            if count > 2: 
                return 0
    else :
        return 1

def solution(n) :
    answer=0
    for i in range(1,n+1) :
        if isprime(i)==1 :
            answer+=1
    return answer
