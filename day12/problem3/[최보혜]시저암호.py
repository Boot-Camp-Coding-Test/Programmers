def solution(s, n):
    l = list('abcdefghijklmnopqrstuvwxyz')
    u = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ss = list(s)
    answer = []
    for i in ss:
        if i in l:
            k = l.index(i)
            answer.append(l[(k+n)%26])
        elif i in u:
            k = u.index(i)
            answer.append(u[(k+n)%26])
        elif i==' ':
            answer.append(' ')
    return ''.join(map(str,answer))
