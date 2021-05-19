def solution(x):
    return not bool(x % eval('+'.join(list(str(x)))))

# eval('1 + 5 + 7') => 13
# 나누어 떨어지면 0으로 반환 => bool함수에 False => not연산자로 True로 변환
