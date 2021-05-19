def solution(x):
    return not bool(x % eval('+'.join(list(str(x)))))
