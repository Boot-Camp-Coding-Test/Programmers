def solution(left, right) :
    answer = 0
    for num in range(left, right+1) :
        divisors = [div for div in range(1, int(num/2)+1) if num%div==0]
        divisors.append(num)
        if len(divisors)%2 == 0 :
            answer += num
        elif len(divisors) != 0:
            answer -= num
    return answer
