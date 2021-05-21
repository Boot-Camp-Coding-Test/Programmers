def solution(n):
    answer = [i if n%i == 0 else 0 for i in range(1,n+1)]
    return sum(answer)
