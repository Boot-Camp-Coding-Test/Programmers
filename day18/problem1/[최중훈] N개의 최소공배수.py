def gcd(n, m):
    if n < m:
        n, m = m, n
    while n % m != 0:
        n, m = m, n%m
    return m

def lcm(n ,m):
    return int(n * m / gcd(n, m))

def solution(arr):
    arr = sorted(arr)
    for i in range(len(arr)-1):
        arr[i+1] = lcm(arr[i], arr[i+1])
    
    return arr[-1]
