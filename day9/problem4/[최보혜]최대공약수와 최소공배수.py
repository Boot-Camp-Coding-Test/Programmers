def solution(n, m):
    mini= 1000000
    for i in range(1, min(n,m)+1):
        if n%i==0 and m%i==0:
            mini = i
    maxi = n*m/mini
    return [mini, maxi]
