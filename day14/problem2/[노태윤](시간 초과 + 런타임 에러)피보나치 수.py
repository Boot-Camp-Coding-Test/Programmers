# 7, 10, 13, 14 - 런타임 에러
# 8, 9, 11, 12 - 시간 초과

def fibo(n,fibo_dict={}) :
    if n in fibo_dict :
        return fibo_dict[n]
    if n == 1 :
        fibo_dict[n] = 1
        return fibo_dict[n]
    elif n == 0 :
        fibo_dict[n] = 0
        return fibo_dict[n]
    else :
        return fibo(n-1,fibo_dict) + fibo(n-2,fibo_dict)

def solution(n):
    answer = fibo(n,fibo_dict={}) % 1234567
    return answer
