# 효율성 통과 안됨
def solution(n):
    num_lst = [i for i in range(1, n+1)]
    cnt = 0
    while num_lst:
        for i in range(len(num_lst) + 1):
            if sum(num_lst[:i]) == n:
                cnt += 1
        num_lst = num_lst[1:]
    return cnt


# 리스트 사용한 것 보다 조금 더 빠르지만 여전히 실패
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        tmp = 0
        for j in range(i, n+1):
            tmp += j
            if tmp == n: 
                cnt += 1    
            elif tmp > n: # 연속되는 수의 합이 더 커지는 경우에 break를 걸어주니까 통과됨
                break
    return cnt
