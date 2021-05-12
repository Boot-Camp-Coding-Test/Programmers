def solution(numbers):
    answer = []
    for idx, n in enumerate(numbers):
        for s in range(len(numbers)):
            if idx != s:
                sum = n + numbers[s]
                answer.append(sum)
    answer = sorted(list(set(answer)))
    
    return answer
