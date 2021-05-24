# 정확성 70.4% 뭐가 틀린건지 모르겠다

def solution(N, stages):    
    finish = [0 for i in range(max(stages)+1)]  # 크기만큼 zero list생성 [0, 0, 0...]
    for i in stages:
        finish[i] += 1  # 인덱스별로 카운팅
    
    arrival = finish.copy()
    for i, v in enumerate(finish):
        for n in range(i):
            arrival[n] += v  # 도달인원 카운팅
        
    fail_, fail = {}, [x/y for x, y in zip(finish, arrival)] # 스테이지 = 인덱스 / 실패율 계산
    for i, v in enumerate(fail):
        if not i in [0, N+1]: # 0번째, 현재나온 스테이지+1번째 예외처리
            fail_[i] = v
    
    sort = sorted(fail_.items(), reverse=True, key=lambda x:x[1])
    return [x[0] for x in sort]
