def gcd(a,b) : # 최대공약수 알고리즘
    if a == 0 :
        return b 
    else :
        return gcd(b%a,a)

def lcm(a,b) : # 최소공배수 알고리즘
    return a * b // gcd(a,b)

def solution(arr):
    while arr : 
        first,second = arr.pop(0),arr.pop(0) # arr 앞에 두개 element의 최소공배수를 구하고 앞 자리에 다시 insert 한 뒤에 계속 업데이트 하기
        lcms = lcm(first,second)
        if not arr : # 만약 마지막 arr 에 
            break
        arr.insert(0,lcms)
    return lcms
