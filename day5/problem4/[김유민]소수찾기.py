def solution(n):
    primes = []
    for num in range(2, n+1) :
        tag = 1
        x = num**0.5

        for d in range(2, int(x)+1) :
            if num%d == 0:
                tag = 0
                break

        if tag == 1 :
            primes.append(num)

    return len(primes)
