from string import ascii_lowercase,digits

def convert(num,base) : # N 진수 구하는 알고리즘
    tmp = digits+ascii_lowercase # ==> 0123456789abcdefghijklmnopqrstuvwxyz
    q,r = divmod(num,base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q,base) + tmp[r]

def solution(n):
    answer = 0
    converted = convert(n,3) # 3진수로 변환
    reversed_string = "".join(reversed(converted)) # 순서 뒤집기
    answer = int(reversed_string,3) # 10진수로 변환
    return answer
