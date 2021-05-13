def solution2(array, commands):
    answer = []
    for s,e,i in commands:
        k = array[s-1:e]
        k.sort()
        answer.append(k[i-1])
    return answer
