def solution(A,B):
    
    a = sorted(A)
    b = sorted(B, reverse=True)
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    
    answer = sum
    return answer


A = [1, 4, 2]	
B = [5, 4, 4]	

print(solution(A,B))
