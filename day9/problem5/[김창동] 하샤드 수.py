# 공간 복잡도
def solution(x):
    return not bool(x % eval('+'.join(list(str(x)))))

def solution(x):
    str_ = list(str(x))   # ['1', '5', '7']
    ev = eval('+'.join(str_)) # eval('1 + 5 + 7') => 13
    return not bool(x % ev) # 나누어 떨어지면 0으로 반환 => bool함수에 False => not연산자로 True로 변환
