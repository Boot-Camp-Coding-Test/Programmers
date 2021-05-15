def solution(seoul):
    for i, j in enumerate(seoul):
        if j == 'Kim':
            return "김서방은 {}에 있다".format(i)
