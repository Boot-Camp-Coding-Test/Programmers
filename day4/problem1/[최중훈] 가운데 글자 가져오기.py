def solution(s):
    answer = ''

    l = len(s)
    index = int(l / 2)
    if l % 2 != 0:
        answer = s[index]
    else:
        answer = s[index-1] + s[index]

    return answer
