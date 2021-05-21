def solution(n):
    n = str(n)
    a = []
    for i in n: #정수n의 각 자리수 리스트 a에 저장
        a.append(i)
    a.sort(reverse=True) #정렬
    a = int(''.join(a)) #리스트를 정수로
    return a
    
    
    
