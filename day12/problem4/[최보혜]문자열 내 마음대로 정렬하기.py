from collections import defaultdict
def solution(strings, n):
    result, answer = defaultdict(list), []
    for i in strings:
        result[i[n]].append(i)
    result = dict(sorted(result.items()))
    
    for i in result.values():
        i.sort()
        answer.append(i)
    answer = sum(answer, [])
    return answer
