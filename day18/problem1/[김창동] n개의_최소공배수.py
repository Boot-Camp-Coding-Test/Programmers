from functools import reduce

def solution(arr):
    div = 2
    l = []

    while max(arr) >= div:   
        arr_ = arr
        arr = [i // div if not i % div else i for i in arr]

        if arr == arr_:
            div += 1
        else:
            l.append(div)
            
    return reduce(lambda x, y: x * y, l)
