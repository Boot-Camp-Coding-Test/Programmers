def solution(n):
    n = str(n)
    answer = []
    for i in range(len(n)-1, -1, -1) :
        print(i, n[i])
        answer.append(int(n[i]))
    return answer
