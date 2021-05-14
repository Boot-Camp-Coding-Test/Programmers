def solution(s):
    answer = True
    s = s.lower()
    p = 0
    y = 0
    for i in s :
        # i 가 'p' 이면 아래 실행
        if i == 'p' :
            p+=1
        # i 가 'y' 이면 아래 실행
        elif i == 'y' :
            y+=1
    # p 와 y 의 갯수가 같다면 아래 실행
    if p == y :
        return True
    # p 와 y 의 갯수가 같지 않다면 아래 실행
    else :
        return False
