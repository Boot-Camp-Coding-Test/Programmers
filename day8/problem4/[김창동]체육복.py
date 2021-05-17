def solution(n, lost, reserve):
    cnt = 0
    
    for i in lost:
        if i-1 in reserve:
            cnt += 1
            reserve.remove(i-1)
            continue

        if i+1 in reserve:
            cnt += 1
            reserve.remove(i+1)

    return n - (len(lost) - cnt) 
