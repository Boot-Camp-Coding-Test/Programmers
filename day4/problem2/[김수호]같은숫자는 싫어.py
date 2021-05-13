def solution(arr):
    res = []
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            res.append(arr[i-1])
    res.append(arr[-1])
    return res
