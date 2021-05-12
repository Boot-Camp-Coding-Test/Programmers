def solution(numbers):
    answer = []
    for n,i in enumerate(numbers):
        for _n,j in enumerate(numbers):
            if n == _n:
                continue
            else :
                answer.append(i+j)
    answer = list(sorted(set(answer)))
    return answer
