def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        list_ = array[i-1:j]
        list_.sort()
        answer.append(list_[k-1])
    return answer
