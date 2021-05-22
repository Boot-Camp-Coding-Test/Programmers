# 재귀 사용
def solution(n):
    three = numeral_system(n, 3)
    return int(three[::-1], 3)
    
def numeral_system(number, base):
    q, r = divmod(number, base)
    n = '0123456789ABCDEF'[r]
    return numeral_system(q, base) + n if q else n

#######################################################

# 재귀 사용x
def solution(num):
    answer = ''
    
    while num >= 1:
        num, rest = divmod(num, 3)
        answer += str(rest)
    return int(answer[::-1])
