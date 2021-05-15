def solution(n):
    if n <= 1:
        return 0
    res, answer = 0, 0
    #num = [i for i in range(1,n+1)]
    for i in range(2,n+1):
        res = i - 2
        for j in range(2, i):
            if i % j != 0:
                res -= 1
        if res == 0:
            answer += 1
    return(answer)
