# 약수의 총 갯수 반환하는 함수
def yaksu(N) :
    yaksu_list = [False] * (N+1)
    for i in range(1,N+1) :
      
        # 이미 약수라고 정의되었다면 그냥 continue
        if yaksu_list[i] == True :
            continue
        
        a = N//i
        b = N%i
        
        # 나누어 떨어진다면 아래 코드 실행
        if b == 0 :
            yaksu_list[i] = True
            yaksu_list[a] = True
    
    # True (약수) 의 갯수 반환
    yaksu_sum = sum(yaksu_list)
    return yaksu_sum

def solution(left, right):
    answer = 0
    for i in range(left,right+1) :
      
        # 약수의 총 갯수가 짝수라면 아래 코드 실행
        if yaksu(i) % 2 == 0 :
            answer+=i
        
        # 약수의 총 갯수가 홀수라면 아래 코드 
        else :
            answer-=i
    return answer
