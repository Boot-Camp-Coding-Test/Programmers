def solution(a):
    x = []
    while a != 0 :
        x.append(a%3)
        a = a//3

    x.reverse()
    answer = [x[i]*3**i for i in range(len(x)-1, -1, -1)]

    return sum(answer)
