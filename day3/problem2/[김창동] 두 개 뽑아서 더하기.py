from itertools import combinations

def solution(numbers):
    answer = [sum(i) for i in list(combinations(numbers, 2))]
    answer = list(set(answer))
    answer.sort()
    return answer
