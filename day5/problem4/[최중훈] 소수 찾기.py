def solution(n):
    answer = 0
    
    if n == 1:
        return answer
    
    for i in range(2, n+1):
        tmp = 0
        for j in range(1, i+1):
            if i % j == 0:
                tmp += 1
        
        if tmp == 2:
            answer += 1
    
    return answer
################### 시간초과로 통과 못함 내일 다시..#####################    


def solution(n):
    num = set(range(2, n+1)) # 2부터 n까지의 집합
    
    # 에라토스테네스의 체 https://ko.wikipedia.org/wiki/에라토스테네스의_체
    # 1. (2 ~ n)의 수 i가 num 집합 안에 있는지 확인
    # 2. i 자신을 제외한 i의 배수를 모두 지워줌 >> range(i*2, n+1, i)에서 "i*2"의 수로 시작해서 "i"간격으로 보는 부분 
    # 3. 최종적으로 소수만 담긴 num set이 생김
    for i in range(2, n+1):
        if i in num:
            num -= set(range(i*2, n+1, i))
        
    answer = len(num)

    return answer
################# 성공 ####################
