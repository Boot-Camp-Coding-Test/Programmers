def solution(n, m):
    def gcd(n, m): # 최대공약수 찾는 재귀함수
        if m == 0:
            return n
        if n < m:
            (n, m) == (m, n)
        return gcd(m, n%m)

    gcd_num = int(gcd(n, m)) # 최대공약수 함수를 사용해서 구한 gcd
    lcm_num = int(n*m / gcd_num) # 두 수를 곱하고 gcd로 나누어주면 lcm
    answer = [gcd_num, lcm_num]

    return answer
