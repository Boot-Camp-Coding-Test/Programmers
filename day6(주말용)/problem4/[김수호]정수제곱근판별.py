# sqrt(n) = n**(1/2)
def solution(n):
    res = n**(1/2)
    if n <= 0:
        return -1
    elif res - int(res) == 0:
        return (res+1) ** 2
    else:
        return -1
