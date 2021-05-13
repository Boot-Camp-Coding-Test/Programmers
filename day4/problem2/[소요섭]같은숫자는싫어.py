def solution(arr):
    answer = []
    arr.append('pad')
    end = len(arr)
    for i in range(1, end):
        if arr[i] != arr[i-1]:
            answer.append(arr[i-1])
    return answer
