def solution(n, lost, reserve):
    lost, reserve = list(set(lost)-set(reserve)), list(set(reserve)-set(lost))
    answer = n-len(lost)
    for i in lost:
        if i-1 in reserve and i not in reserve:
            reserve.remove(i-1)
            answer+=1
        elif i+1 in reserve and i not in reserve:
            reserve.remove(i+1)
            answer+=1
    return answer
