def solution(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        result.append([x+y for x, y in zip(a, b)])
        
    return result
