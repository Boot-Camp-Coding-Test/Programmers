def solution(n, lost, reverse) :
    for i in (list(set(lost) & set(reverse))): ##여벌의 체육복이 있으나, 본인이 잃어버린 경우. 어차피 나누어 줄 수 없기 때문에 lost,reverse에서 제거
        lost.remove(i)
        reverse.remove(i)
    


    for i in reverse :
        if i-1 in lost :
            lost.remove(i-1)

        elif i+1 in lost :
            lost.remove(i+1)

        else :
            continue
    return n - len(lost)