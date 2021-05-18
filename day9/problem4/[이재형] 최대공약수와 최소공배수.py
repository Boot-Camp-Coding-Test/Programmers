def solution(n, m):
    answer = []
    a = [i for i in range(1, n+1) if n % i == 0]
    b = [i for i in range(1, m+1) if m % i == 0]
    c = list(set(a) & set(b))
    answer.append(max(c))
    
    
    for i in range(1, 10000000):
        if (i % n == 0) and (i % m == 0):
            answer.append(i)
            break
    
    return answer
