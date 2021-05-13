def solution(s):
    b = list(s)
    a = len(b)
    c = []
    if a%2 == 0:
        c.append(b[a//2 - 1])
        c.append(b[a//2])
    else:
        c.append(b[a//2])
    return ''.join(c)
