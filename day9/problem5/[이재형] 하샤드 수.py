def solution(x):
    a = []
    for i in range(len(str(x))):
        a.append(int(str(x)[i]))

    if x % sum(a) == 0:
        return True
    else :
        return False
