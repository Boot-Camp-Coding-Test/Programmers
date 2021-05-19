def solution(x):
    tmp_lst = [i for i in str(x)]

    if x % sum(list(map(int, tmp_lst))) == 0:
        return True
    else:
        return False
