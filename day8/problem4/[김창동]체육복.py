# 1차 마지막 문제 오답
def solution(n, lost, reserve):
    cnt = 0
    
    for i in lost:
        if i in reserve:
            cnt += 1
            reserve.remove(i)
            continue
        
        if i-1 in reserve:
            cnt += 1
            reserve.remove(i-1)
            continue

        if i+1 in reserve:
            cnt += 1
            reserve.remove(i+1)

    return n - (len(lost) - cnt)

# 2차 통과
def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)    # 중복 제거
    
    for i in reserve:   # 리턴값 간소화를 위해 대여인원에서 값 찾기
        if i-1 in lost:
            lost.remove(i-1)
            continue

        if i+1 in lost:
            lost.remove(i+1)

    return n - len(lost)
