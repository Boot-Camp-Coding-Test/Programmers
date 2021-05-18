def solution(n, lost, reserve):
    reserve_lst = list(set(reserve) - set(lost)) # 여벌 있는 사람 중에 잃어버린 사람 삭제
    lost_lst = list(set(lost) - set(reserve)) # 잃어버린 사람 중에 여벌 있는 사람 삭제

    count = n - len(lost_lst)
    for i in lost_lst:
        if i-1 in reserve_lst:
            count += 1
            reserve_lst.remove(i-1)
        
        elif i+1 in reserve_lst:
            count += 1
            reserve_lst.remove(i+1)
    
    return count
