def solution(n):
    list = []
    for i in range(0,n):
        if i < 2:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])
            
    return list[n-1]
