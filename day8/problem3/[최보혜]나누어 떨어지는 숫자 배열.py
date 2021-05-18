def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0 and i not in answer:
            answer.append(i)
    answer.sort()
    if len(answer) ==0:
        return [-1]
    else:
        return answer
