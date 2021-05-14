def solution3(a, b):
    x, y = min(a,b), max(a,b)
    answer = [i for i in range(x,y+1)]
    return sum(answer)
