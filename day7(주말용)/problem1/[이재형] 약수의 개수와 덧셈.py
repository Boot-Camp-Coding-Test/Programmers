def solution(left, right):
    answer = []
    a = [number for number in range(left, right+1)]

    for no in a :
        if len([i for i in range(1, no+1) if no % i == 0]) % 2 == 0:
            answer.append(no)
        else :
            answer.append(-no)

    return sum(answer)