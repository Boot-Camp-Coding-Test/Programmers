def solution(s, n):
    answer = ''

    for i in list(s):
        caesar = ord(i) + n  # 바뀔 값, 시저 값
                    
        if ord(i) < 91:    # 대문자인가?
            if caesar > 90:
                caesar = caesar % 90 + 64
        else:
            if caesar > 122:
                caesar = caesar % 122 + 96
        
        if i == ' ':
            answer += i        
        else:
            answer += chr(caesar)
    return answer
