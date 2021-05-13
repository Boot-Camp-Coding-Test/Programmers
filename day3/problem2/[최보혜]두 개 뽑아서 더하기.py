from itertools import combinations
def solution(numbers):
    answer = []
    l = list(set(combinations(numbers,2)))
    for i in l:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    return answer
