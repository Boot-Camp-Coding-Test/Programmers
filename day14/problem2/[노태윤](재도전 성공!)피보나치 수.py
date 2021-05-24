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

# ========================================================
# 재도전

def solution(n):
    fibo_list = [0] * (n+1) 
    fibo_list[1] = 1 
    for i in range(2,n+1) :
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    answer = fibo_list[n] % 1234567
    return answer

# Key points
    # 수업 때 배웠던 재귀 방식으로 풀어봤는데 런타임 에러 + 시간 초과가 뜸
    # 동적 할당까지 썼는데 에러 뜸..
    
    # 재귀의 단점
        # 재귀의 깊이가 충분히 깊어졌을 때 stack overflow 가 발생한다고 함
        # 아마 이런 문제점 때문이지 않을까 싶음..
    
    # 단순 반복문으로 문제 해결!
