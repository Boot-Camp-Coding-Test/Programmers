def solution(s):
    answer = []
    for i in s:
        answer.append(i)
    answer.sort(reverse=True)
    answer = ''.join(answer)
    return answer
