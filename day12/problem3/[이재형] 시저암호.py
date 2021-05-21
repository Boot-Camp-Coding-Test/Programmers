def solution(s, n):
    answer = ''
    b = s.upper()
    x = []
    for i in range(len(s)):
        if ord(list(s)[i]) == 32:
            answer = answer + chr(32)

        elif ord(list(b)[i])+n > 90 :
            a = list(b)[i]
            answer = answer + chr(ord(a)+n+6).upper()

        else :
            a = list(b)[i]
            answer = answer + chr(ord(a)+n)


    for i in range(len(s)) :
        if list(s)[i].islower() :
            x.append(answer[i].lower())
        else :
            x.append(answer[i])




    return ''.join(x)
