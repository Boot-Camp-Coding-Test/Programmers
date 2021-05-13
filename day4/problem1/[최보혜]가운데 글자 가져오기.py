def solution(s):
    answer = list(s)
    if len(answer)%2==1:
        return ''.join(map(str,answer[len(answer)//2]))
    else:
        return ''.join(map(str,answer[len(answer)//2-1:len(answer)//2+1]))
