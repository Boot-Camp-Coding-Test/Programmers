def solution(n):
    tmp_lst = []
    while True: # n != 0
        if n < 3:
            tmp_lst.append(n)
            break
        tmp_lst.append(n % 3)
        n = n // 3
    
    tmp_lst.reverse()

    answer = 0
    for i in range(len(tmp_lst)):
        answer += tmp_lst[i] * (3**i)
        
    return answer
