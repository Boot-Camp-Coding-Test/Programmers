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

# =================================
# 재도전

def solution(n):
    # 처음에는 다 True 값 담기
    # True 가 소수를 의미
    sieve = [True] * (n+1)
    
    # 0 과 1 은 소수가 아니므로 False
    sieve[0] = False
    sieve[1] = False
    
    # n 의 최대 약수가 sqrt(n) 이하 임
    m = int(n**0.5)
    
    # 아래 코드 해석 참고
    for i in range(2,m+1) :
        if sieve[i]==True :
            for j in range(i+i,n+1,i) :
                sieve[j]=False
    
    # True 값의 합 반환
    answer = sum(sieve)
    return answer

# Key Points
  # 예를 들어 n 은 10 이라고 가정
  
  # 처음 sieve 리스트
  #    0      1      2    3     4     5      6     7     8     9    10
  # [False, False, True, True, True, True, True, True, True, True, True]
  
  # m : int(sqrt(10)) ==> 3 
  
  # 2 부터 3 까지 for loop 진행
      # i 가 2 일 때
          # i+i (2+2=4) 부터 10까지 i(2) 씩 증가
              # 4, 6, 8, 10 은 False 가 됨
      
      # i 가 3 일 때
          # i+i (3+3=6) 부터 10까지 i(3) 씩 증가
              # 6, 9 는 False 가 됨
  
  # 결국 sieve 는 
  #    0      1      2     3     4      5     6      7     8      9     10
  # [False, False, True, True, False, True, False, True, False, False, False]
  
  # 여기서 sum(sieve) 하면 True 의 총 갯수 반환
