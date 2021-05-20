def collatz(num,counts=0) :
    if counts >=500 :
        return -1
    if num == 1 :
        return counts
    if num % 2 == 0 :
        num/=2
    else :
        num = num * 3 + 1
    counts+=1
    return collatz(num,counts)

def solution(num):
    answer = collatz(num,counts=0)
    return answer
