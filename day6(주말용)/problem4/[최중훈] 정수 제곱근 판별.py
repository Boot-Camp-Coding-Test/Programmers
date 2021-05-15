def solution(n):
    if n**0.5 == int(n**0.5):
        x =  n ** 0.5
        return int((x+1)**2)
    else:
        return  -1
