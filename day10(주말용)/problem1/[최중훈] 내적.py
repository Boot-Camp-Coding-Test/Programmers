def solution(a, b):
    lst = []
    for i, j in zip(a, b):
        lst.append(i*j)
    
    return sum(lst)
