def solution(x):
    num = sum(list(map(int, str(x))))
    if x%num==0:
        return True
    else:
        return False
