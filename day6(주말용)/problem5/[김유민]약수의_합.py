def solution(n):
    divisors = [div for div in range(1, int(n/2)+1) if n%div==0]
    divisors.append(n)
    return sum(divisors)
