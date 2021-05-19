def solution(n, arr1, arr2):
    a=[bin(x)[2:].zfill(n) for x in arr1]
    b=[bin(x)[2:].zfill(n) for x in arr2]
    print(a)
    print(b)
    answer=[]
    for x,y in zip(a,b):
        e=""
        for c,d in zip(x,y):
            if int(c)+int(d) ==0:
                e+=" "
            else :
                e += "#"
        answer.append(e)
    return answer
