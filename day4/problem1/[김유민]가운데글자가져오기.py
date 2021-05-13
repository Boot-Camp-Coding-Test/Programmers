def solution(s):
    l = int(len(s)/2)
    if len(s)%2 != 0:
        answer = s[l]
    else :
        answer = s[l-1:l+1]
    return answer
