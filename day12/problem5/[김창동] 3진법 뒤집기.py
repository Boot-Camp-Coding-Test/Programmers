def solution(n):
    three = numeral_system(n, 3)
    return int(three[::-1], 3)
    
def numeral_system(number, base):
    q, r = divmod(number, base)
    n = '0123456789ABCDEF'[r]
    return numeral_system(q, base) + n if q else n
