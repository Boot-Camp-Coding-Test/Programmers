def solution(s, n):
    ascii = [ord(i) for i in s]
    tocha = []
    for a in ascii:
        if a == 32:
            tocha.append(' ')
        elif 91<=a+n<=91+n:
            tocha.append(a+n-26)
        elif 123<=a+n:
            tocha.append(a+n-26)
        else:
            tocha.append(a+n)       
    chrlist = [chr(i) if i !=' ' else ' '  for i in tocha]

    return "".join(chrlist)
