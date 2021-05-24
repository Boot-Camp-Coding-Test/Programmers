def solution(s):
    l = list(s.split(' ',-1))
    answer = []
    for i in l:
        k = [i[k].upper() if k%2==0 else i[k].lower() for k in range(len(i))]
        answer.append(''.join(map(str, k)))
    print(' '.join(map(str,answer)))
    return ' '.join(map(str,answer))
