def solution(s):
    py = [i for i in s.lower()]
    p = py.count('p')
    y = py.count('y')
    if p == y:
        answer = True
    else:
        answer = False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
