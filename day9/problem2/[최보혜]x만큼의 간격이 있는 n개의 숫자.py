def solution(x, n):
    answer = [x]
    i = 2
    while len(answer)!=n:
        answer.append(x*i)
        i+=1
    return answer
