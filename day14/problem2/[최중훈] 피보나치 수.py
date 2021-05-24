def solution(n):    
    if n == 1:
        return 1 % 1234567
    else:
        tmp = n
        lst = [0, 1]
        while tmp > 1:
            lst.append(lst[-2] + lst[-1])
            tmp = tmp - 1
    return lst[n] % 1234567
