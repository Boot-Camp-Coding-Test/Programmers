import re

def solution(dartResult):    
    num = list(map(int, re.findall('[0-9]', dartResult))) # 숫자 추출
    for i in range(3): # 숫자 [0, 1, 0..] 처리
          if num[i] == 1 and num[i+1] == 0:
                num[i] = 10
                del num[i+1]
                
    bonus = re.split('[0-9]', dartResult) # 보너스, 옵션 추출
    bonus = list(filter(None, bonus))     # 빈문자열 제거
    opt = [1, 1, 1] # 옵션 저장소
    
    for i, v in enumerate(bonus):
        if v[0] == 'D':   # 보너스 계산
            num[i] **= 2
        elif v[0] == 'T':
            num[i] **= 3

        if len(v) > 1:    # 옵션이 있을때
            if v[1] == '*':
                 opt[i] = 2
            else:
                opt[i] = -1

    for i, v in enumerate(opt):  # 옵션 
        if v == 2 and i > 0:     # 첫번째 제외 스타상값 계산
            opt[i-1] *= 2

    # ex) '1S2D*3T' => num[1, 4, 27] / opt= [2, 2, 1]
    return sum([x*y for x, y in zip(num, opt)]) # sum([1 * 2, 4 * 2, 27 * 1])
