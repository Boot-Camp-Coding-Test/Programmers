def check(a,n) :
    b = a  
    while True :
        if a > n : # n 넘어가면 0 반환
            return 0
        elif a == n : # n 이 되면 1 반환
            return 1
        b+=1 # 1 씩 증가
        a = a + b # 계속 더하기

def solution(n):
    answer=0
    for i in range(1,n+1) : 
        answer+=check(i,n) # 계속 더해주기
    return answer
