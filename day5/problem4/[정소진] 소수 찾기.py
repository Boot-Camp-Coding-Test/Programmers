# 1
def solution(n): # 시간 초과 ㅎ..
  
    cnt = 0

    for i in range(2, n+1):
        if i == 2 or i == 3:
            cnt += 1
        
        else :
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    break

            if prime:
                cnt += 1
            
    return cnt
  
  
  # 2
  def solution(n):
    
    prime = [False, False] + [True] * (n-1) # 0과 1은 소수가 아니므로 False, 2는 소수이므로 나머지는 일단 True로 채워준다.
    
    for i in range(2, n+1):                 # 2부터 n까지의 숫자가 담긴 리스트를 순회
        if prime[i]:                        # 처음에는 prime[2]가 들어감 => prime[2] = True => 소수
            for j in range(2*i, n+1, i):    # 처음에는 2*2 부터 n까지의 숫자가 담긴 리스트를 2간격으로 순회
                prime[j] = False            # j => 4 8 10 12 14 16 ... => 소수가 아니므로 False로 바꿔줌
                                            # 소수의 배수는 소수가 아님을 이용한 방법
    
    return prime.count(True)                # 리스트 prime에서 True의 개수를 반환해준다.
