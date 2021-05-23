def solution(n):
    for num in range(1, n+1) : #1부터 n까지의 정수 num에 대해
        if num**2 > n : #num의 제곱이 n을 초과하면 break하여 return -1
            break
        elif num**2 == n : #num의 제곱이 n이면 요구하는 숫자(num+1의 제곱) 반환
            return (num+1)**2
        
    return -1
